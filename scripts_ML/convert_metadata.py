import pandas as pd

# Read metadata
metadata = pd.read_csv("GSE7621_series_matrix.txt", sep="\t", skiprows=29, index_col=0, low_memory=False)

# Transpose DataFrame，set sample ID as index
metadata = metadata.T

# Ensure `!Sample_geo_accession` exists，they are sample ID（GSMxxxxx）
if "!Sample_geo_accession" in metadata.columns:
    sample_ids = metadata["!Sample_geo_accession"].values
else:
    raise KeyError("Metadata file does not contain '!Sample_geo_accession' column!")

# Obtain sample label （'normal'  or 'PD'）
sample_labels = metadata.index.values

# Create DataFrame
metadata_clean = pd.DataFrame({"sample_id": sample_ids, "label": sample_labels})

# Modify PD vs. Normal labels
metadata_clean["label"] = metadata_clean["label"].apply(lambda x: "PD" if "PD" in x else "Normal")

# save  metadata
# metadata_clean.to_csv("GSE7621_metadata.txt", sep="\t", index=False)

print(metadata_clean.tail())
