import pandas as pd

# Load log_transformed data (expr_df) and DEGs data (degs_df)
expr_df = pd.read_csv("GSE7621_RMA_normalized.txt", sep='\t', index_col=0)
degs_df = pd.read_csv("significant_DEGs_clean_results.csv", index_col=0)

# Obtain DEGs ProbeID (Column Gene)
deg_probes = set(degs_df["Gene"])

"""
Why use set( ) to extract Probe ID?
a) Speed up lookup
Sets in Python use a hash table to store data, so the time complexity for looking up an element is O(1), 
whereas the lookup time complexity for pandas.Series or list is typically O(n).

If expr_df.index is large, for example, containing tens of thousands of Probe IDs, and degs_df["Gene"] 
only contains a few hundred DEGs, using a set for intersection operations (intersection()) 
will be faster than directly using pandas.Series.

b) Remove duplicate values
If there are duplicate probe IDs in degs_df["Gene"], converting it to a set() will automatically deduplicate 
(keeping only unique values). This avoids generating duplicate rows during subsequent filtering.

c) Using .intersection() is more intuitive
When deg_probes is a set, we can directly use set.intersection() to find the intersection.
"""

# Filter matched Probe ID of DEGs in the expr_df
filtered_expr_df = expr_df.loc[expr_df.index.intersection(deg_probes)]

# Create a mapping dictionary from Probe ID to GeneSymbol
gene_symbol_map = dict(zip(degs_df["Gene"], degs_df["GeneSymbol"]))

# Rename index
filtered_expr_df.rename(index=gene_symbol_map, inplace=True)

# Transpose index and column names
final_expr_df = filtered_expr_df.T

# Load Metadata to get Label
metadata_df = pd.read_csv("GSE7621_metadata.txt", sep="\t", index_col=0)

## Confirm index from two dataframe are the same
# print(metadata_df.index.equals(final_expr_df.index))

# Merge Label of metadata to final_expr_df
final_expr_df["label"] = metadata_df["label"]

# Save the file
final_expr_df.to_csv("final_expr_df.csv")