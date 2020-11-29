# Load bioactivity data
import pandas as pd

df3 = pd.read_csv('acetylcholinesterase_04_bioactivity_data_3class_pIC50.csv')

selection = ['canonical_smiles','molecule_chembl_id']
df3_selection = df3[selection]
df3_selection.to_csv('molecule.smi', sep='\t', index=False, header=False)

# === Calculate fingerprint descriptors ===
# Calculate PaDEL descriptors (TERMINAL COMMANDS)
# cat padel.sh
# bash padel.sh
# ls -l


# === Preparing the X and Y Data Matrices ===
# X data matrix
df3_X = pd.read_csv('descriptors_output.csv')

df3_X = df3_X.drop(columns=['Name'])

# Y variable
# Convert IC50 to pIC50
df3_Y = df3['pIC50']
dataset3 = pd.concat([df3_X,df3_Y], axis=1)

# Combining X and Y
dataset3.to_csv('acetylcholinesterase_06_bioactivity_data_3class_pIC50_pubchem_fp.csv', index=False)
