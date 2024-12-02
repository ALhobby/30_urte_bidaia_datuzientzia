import polars as pl
import matplotlib.pyplot as plt

"""
Oinarrizko emaitzak
"""

file = "/home/antton/Projects/30_urte_bidaia_datuzientzia/bigarren_fasea_emaitzak.tsv"
df = pl.read_csv(file, separator="\t", has_header=True)


# Remove column "nor", give the sum of the votes for each country and sort the countries by the sum of the votes
nums_only_df = df.drop("nor")

# Sum the votes for each country, rank from highest to lowest
sums = nums_only_df.sum().transpose(include_header=True).sort("column_0", descending=True)

# Calculate average votes for each country (so divided by 17)
sums_and_averages = sums.with_columns((pl.col("column_0") / 17).alias("average"))

# Rename "column_0" to "guztira"
sums_and_averages = sums_and_averages.rename({"column": "herrialdea", "column_0": "guztira"})

sums_and_averages.head(15).write_csv("bigarren_fasea_TOP15.tsv", separator="\t", include_header=True)

print(sums_and_averages.head(10))

# Plot the top 10 countries
plt.figure(figsize=(10, 5))
bars = plt.bar(sums_and_averages.head(10).to_pandas()["herrialdea"], sums_and_averages.head(10).to_pandas()["guztira"])
plt.ylim(0, 85)

plt.xlabel("Herrialdea")
plt.ylabel("Boto guztira")
plt.title("Top 10 herrialdeak botoen arabera")
plt.xticks(rotation=45)

# Annotate the bar values
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # Center text horizontally
        height + 0.5,                      # Slightly above the bar
        str(height),                       # The value of the bar
        ha="center", va="bottom", fontsize=10
    )

plt.tight_layout()

plt.savefig("bigarren_fasea_TOP10.png", dpi=300)
