# Make sure you do:
# pip install chembl_webresource_client in the terminal
# before running the code
# add print statements anywhere you see fit

# Import necessary libraries
import pandas as pd
from chembl_webresource_client.new_client import new_client

# Target search for coronavirus
target = new_client.target
target_query = target.search('aromatase')
targets = pd.DataFrame.from_dict(target_query)


# Select and retrieve bioactivity data for SARS coronavirus 3C-like proteinase (fifth entry)
selected_target = targets.target_chembl_id[4]
activity = new_client.activity
res = activity.filter(target_chembl_id=selected_target).filter(standard_type="IC50")
df = pd.DataFrame.from_dict(res)
print(df.head(3))
df.standard_type.unique()
df.to_csv('bioactivity_data.csv', index=False)


# Handling missing data
df2 = df[df.standard_value.notna()]


# Data pre-processing of the bioactivity data
# Labeling compounds as either being active, inactive or intermediate
bioactivity_class = []
for i in df2.standard_value:
  if float(i) >= 10000:
    bioactivity_class.append("inactive")
  elif float(i) <= 1000:
    bioactivity_class.append("active")
  else:
    bioactivity_class.append("intermediate")
    
# Iterate the molecule_chembl_id to a list
mol_cid = []
for i in df2.molecule_chembl_id:
  mol_cid.append(i)
  
# Iterate canonical_smiles to a list
canonical_smiles = []
for i in df2.canonical_smiles:
  canonical_smiles.append(i)
  
# Iterate standard_value to a list
standard_value = []
for i in df2.standard_value:
  standard_value.append(i)
  
# Combine the 4 lists into a dataframe
data_tuples = list(zip(mol_cid, canonical_smiles, bioactivity_class, standard_value))
df3 = pd.DataFrame( data_tuples,  columns=['molecule_chembl_id', 'canonical_smiles', 'bioactivity_class', 'standard_value'])
print(df3)

# Alternate method
selection = ['molecule_chembl_id', 'canonical_smiles', 'standard_value']
df3 = df2[selection]

pd.concat([df3,pd.Series(bioactivity_class)], axis=1)

# Save dataframe to CSV
df3.to_csv('bioactivity_preprocessed_data.csv', index=False)