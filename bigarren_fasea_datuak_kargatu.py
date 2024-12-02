import polars as pl

herrialde_zerrenda = [
    "Brasil",
    "Cuba",
    "Panama",
    "Colombia",
    "Republica Dominicana",
    "Puerto Rico",
    "Txina",
    "Vietnam",
    "Uzbekistan",
    "Japonia",
    "Indonesia",
    "Hego Afrika",
    "Azoreak",
    "Bolivia",
    "Myanmar",
    "Cabo Verde",
    "Georgia",
    "Groenlandia",
    "Hego Korea",
    "Ecuador",
    "Islandia",
    "Turkia"
]

print(len(herrialde_zerrenda))

andoni = {"Georgia": 10,
          "Txina": 9,
          "Brasil": 8,
          "Puerto Rico": 7,
          "Cuba": 6,
          "Republica Dominicana": 5,
          "Panama": 4,
          "Colombia": 3,
          "Turkia": 2}

amaia = {"Colombia": 10,
         "Brasil": 9,
         "Indonesia": 8,
         "Hego Afrika": 7,
         "Vietnam": 6,
         "Ecuardor": 5,
         "Panama": 4,
         "Japonia": 3,
         "Puerot Rico": 2}

beñat = {"Cabo Verde": 10,
         "Vietnam": 9,
         "Republica Dominicana": 8,
         "Puerto Rico": 7,
         "Ecuador": 6,
         "Indonesia": 5,
         "Brasil": 4,
         "Cuba": 3,
         "Colombia": 2}

lide = {"Cabo Verde": 10,
        "Republica Dominicana": 9,
        "Colombia": 8,
        "Puerto Rico": 7,
        "Brasil": 6,
        "Uzbekistan": 5,
        "Indonesia": 4,
        "Azoereak": 3,
        "Bolivia": 2}

ekain = {"Panama": 10,
         "Cuba": 9,
         "Colombia": 8,
         "Republica Dominicana": 7,
         "Uzbekistan": 6,
         "Azoreak": 5,
         "Bolivia": 4,
         "Georgia": 3,
         "Turkia": 2}

andrea = {"Panama": 10,
          "Puerto Rico": 9,
          "Cuba": 8,
          "Brasil": 7,
          "Colombia": 6,
          "Indonesia": 5,
          "Boleivia": 4,
          "Republica Dominicana": 3,
          "Ecuardor": 2}

xabier_d = {"Cabo Verde": 10,
            "Vietnam": 9,
            "Indonesia": 8,
            "Republica Dominicana": 7,
            "Brasil": 6,
            "Japonia": 5,
            "Puerto Rico": 4,
            # 3korik ez
            "Panama": 2}

lorea = {"Colombia": 10,
         "Hego Korea": 9,
         "Panama": 8,
         "Japonia": 7,
         "Trukia": 6,
         "Uzbekistan": 5,
         "Boleivia": 4,
         "Azoreak": 3,
         "Islandia": 2}

paul = {"Panama": 10,
        "Colombia": 9,
        "Republica Dominicana": 8,
        "Puerto Rico": 7,
        "Boleivia": 6,
        "Azoreak": 5,
        "Cabo Verde": 4,
        "Georgia": 3,
        "Ecuardor": 2}

cristina = {"Cuba": 10,
            "Indonesia": 9,
            "Groealndia": 8,
            "Hego Afrika": 7,
            "Txina": 6,
            "Islandia": 5,
            "Boliivia": 4,
            "Colombia": 3,
            "Panama": 2,
            "Cabo Verde": 2}  # 2 aldiz 2ko botoa!

antton = {"Groenlandia": 10,
          "Uzbekistan": 9,
          "Txina": 8,
          "Vietnam": 7,
          "Hego Korea": 6,
          "Japonia": 5,
          "Islandia": 4,
          "Cuba": 3,
          "Azoreak": 2}

nahikari = {"Colombia": 10,
            "Japonia": 9,
            "Heog Korea": 8,
            "Eguardor": 7,
            "Uzbekistan": 6,
            "Panama": 5,
            "Georgia": 4,
            "Brasil": 3,
            "Cuba": 2}

josu = {"Uzbekistan": 10,
        "Georgia": 9,
        "Turkia": 8,
        "Txina": 7,
        "Japonia": 6,
        "Azoreak": 5,
        "Cabo Verde": 4,
        "Islandia": 3,
        "Boleivia": 2}

leire_r = {"Hego Korea": 10,
           "Txina": 9,
           "Japonia": 8,
           "Cuba": 7,
           "Vietnam": 6,
           "Cabo Verde": 5,
           "Indonesia": 4,
           "Puerot Rico": 3,
           "Azoreak": 3,  # 2 aldiz 3ko botoa!
           "Georgia": 2}

xabier_m = {"Uzbekistan": 10,
            "Brasil": 9,
            "Txina": 8,
            "Vietnam": 7,
            "Cuba": 6,
            "Turkia": 5,
            "Ecuardor": 4,
            "Georgia": 3,
            "Bolivia": 2}

mireia = {"Uzbekistan": 10,
          "Indonesia": 9,
          "Panama": 8,
          "Cabo Verde": 7,
          "Cuba": 6,
          "Bolivia": 5,
          "Republica Dominicana": 4,
          "Txina": 3,
          "Azoreak": 2}

leire_v = {"Brasil": 10,
           "Panama": 9,
           "Cuba": 8,
           # 7 ez
           "Uzbekistan": 6,
           "Republica Dominicana": 5,
           "Txina": 4,
           "Vietnam": 3,
           "Indonesia": 2}

# Create a DataFrame from a dictionary

# First, fill out all missing countries with 1 in each personal dictionary
izenak = [andoni, amaia, beñat, lide, ekain, andrea, xabier_d, lorea, paul, cristina, antton, nahikari, josu, leire_r, xabier_m, mireia, leire_v]
izenak_str = ["andoni", "amaia", "beñat", "lide", "ekain", "andrea", "xabier_d", "lorea", "paul", "cristina", "antton", "nahikari", "josu", "leire_r", "xabier_m", "mireia", "leire_v"]

for i, voter in enumerate(izenak):
    for country in herrialde_zerrenda:
        if country not in voter:
            voter[country] = 1
    voter["nor"] = izenak_str[i]

# Now, create the DataFrame
df = pl.DataFrame({x: 0 for x in herrialde_zerrenda})

# Add column "nor" in front
df = df.with_columns(pl.lit('').alias("nor"))

# Change the order of the columns
df = df.select(["nor"] + herrialde_zerrenda)

# Fill in the data by appending the dictionaries
for voter in izenak:
    df = df.vstack(pl.from_dict(voter).select(["nor"] + herrialde_zerrenda))

# Remove the first row, which is empty
df = df.slice(1, df.height)

print(df)

# Save the DataFrame to a CSV file
df.write_csv("bigarren_fasea_emaitzak.tsv", separator="\t", include_header=True)
