import polars as pl
import matplotlib.pyplot as plt
import numpy as np

"""
Lehenengoaren antzeko, baina metrika ezberdinak erabiliz

"""

file = "/datuak/bigarren_fasea_emaitzak.tsv"
df = pl.read_csv(file, separator="\t", has_header=True)

# Remove column "nor", give the sum of the votes for each country and sort the countries by the sum of the votes
nums_only_df = df.drop("nor")

# Count how many 10s are in each column
tens_dict = {}
for country in nums_only_df.columns:
    tens_dict[country] = nums_only_df.filter(pl.col(country).eq(10)).height

print(tens_dict)

# Count how many 9s are in each column
nines_dict = {}
for country in nums_only_df.columns:
    nines_dict[country] = nums_only_df.filter(pl.col(country).eq(9)).height

print(nines_dict)

# Count how many 8s are in each column
eights_dict = {}
for country in nums_only_df.columns:
    eights_dict[country] = nums_only_df.filter(pl.col(country).eq(8)).height

print(eights_dict)

# Create new dataframes from the dictionaries
tens_df = pl.DataFrame(tens_dict)
# Add column "domina" with value "Urrea"
tens_df = tens_df.with_columns(pl.lit("Urrea").alias("domina"))

nines_df = pl.DataFrame(nines_dict)
# Add column "domina" with value "Zilarra"
nines_df = nines_df.with_columns(pl.lit("Zilarra").alias("domina"))

eights_df = pl.DataFrame(eights_dict)
# Add column "domina" with value "Brontzea"
eights_df = eights_df.with_columns(pl.lit("Brontzea").alias("domina"))

# Vstack
pre_olympic_df = tens_df.vstack(nines_df).vstack(eights_df)
olympic_df = pre_olympic_df.transpose(include_header=True)

# Rename columns based on the values of the last row
olympic_df = olympic_df.rename({"column": "herrialdea", "column_0": "Urrea", "column_1": "Zilarra", "column_2": "Brontzea"})

# Drop row where herrialdea is 'domina'
olympic_df = olympic_df.filter(pl.col("herrialdea").ne("domina"))

# Sort rows based on Urrea, Zilarra and Brontzea
olympic_df = olympic_df.sort(["Urrea", "Zilarra", "Brontzea"], descending=[True, True, True])

print(olympic_df)

# Save the DataFrame to a tsv file
olympic_df.write_csv("bigarren_fasea_olimpiadak.tsv", separator="\t", include_header=True)

# Get the top 10 countries
pandas_olympic_df = olympic_df.head(10).to_pandas()
print(pandas_olympic_df)

# Ensure numerical data types for medal counts
pandas_olympic_df[["Urrea", "Zilarra", "Brontzea"]] = pandas_olympic_df[["Urrea", "Zilarra", "Brontzea"]].astype(int)

# Define x-axis positions
X_axis = np.arange(len(pandas_olympic_df))

# Create the plot
plt.figure(figsize=(10, 5))

bar_width = 0.3
# Plot the bars with proper alignment
bar1 = plt.bar(X_axis - bar_width, pandas_olympic_df["Urrea"], width=bar_width, color="gold", label="Urrea")
bar2 = plt.bar(X_axis, pandas_olympic_df["Zilarra"], width=bar_width, color="silver", label="Zilarra")
bar3 = plt.bar(X_axis + bar_width, pandas_olympic_df["Brontzea"], width=bar_width, color="peru", label="Brontzea")

# Add labels and ticks
plt.xticks(X_axis, pandas_olympic_df["herrialdea"], rotation=0, ha="center")
plt.xlabel("Herrialdea")
plt.ylabel("Dominak")
plt.title('Top 10 Herrialdeak "dominei" dagokienez')

# Adjust y-axis to show integer values only
max_medal_count = pandas_olympic_df[["Urrea", "Zilarra", "Brontzea"]].max().max()
plt.yticks(range(0, max_medal_count + 2))  # +2 for a small buffer above the max count

# Add counts on top of bars
for bar_group in [bar1, bar2, bar3]:
    for bar in bar_group:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,  # Center text horizontally
            height + 0.1,                      # Position slightly above the bar
            str(height),                       # Text content (the value)
            ha="center", va="bottom", fontsize=10
        )

plt.legend()

# Display the plot
plt.tight_layout()

# Save the plot to a file
plt.savefig("emaitzak/bigarren_fasea_olimpiadak.png", dpi=300)
