import polars as pl
import matplotlib.pyplot as plt

"""
Txorakeriak. Adb, zeinek "asmatu" du gehien bere botoekin? Bozkatutatko zenbat herrialde sartu ta TOP 10ean?
"""

file = "/datuak/bigarren_fasea_emaitzak.tsv"
df = pl.read_csv(file, separator="\t", has_header=True)

top_15_file = "/emaitzak/bigarren_fasea_TOP15.tsv"
top_15_df = pl.read_csv(top_15_file, separator="\t", has_header=True)

top_10_df = top_15_df.head(10)
top_10_list = top_10_df.select(["herrialdea"]).to_series().to_list()

# Zeinek bozkatu ditu top 10eko herrialdeak gehienetan?
df_top_10_bakarrik = df.select(["nor"] + top_10_list)
print(df_top_10_bakarrik)

# Count non-1 values in each row (other than "nor") and add it as a column
columns_subset = df_top_10_bakarrik.columns[1:]

bozkatuak_top10ean_df = df_top_10_bakarrik.with_columns(
    pl.struct(columns_subset)
    .map_elements(lambda row: sum(value != 1 for value in row.values()), return_dtype=pl.Int64)
    .alias("bozkatuak_top10ean")
)

# Sort by bozkatuak_top10ean
bozkatuak_top10ean_df = bozkatuak_top10ean_df.sort("bozkatuak_top10ean", descending=True)

# Sort columns so bozkatuak_top10ean is the second
bozkatuak_top10ean_df = bozkatuak_top10ean_df.select(["nor", "bozkatuak_top10ean"] + top_10_list)

print(bozkatuak_top10ean_df)

# Save to file
bozkatuak_top10ean_df.write_csv("emaitzak/bigarren_fasea_bozkatuak_top10ean.tsv", separator="\t", include_header=True)
