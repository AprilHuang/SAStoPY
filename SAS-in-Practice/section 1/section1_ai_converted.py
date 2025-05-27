import pandas as pd

# Creating the temporary dataset (in memory)
data = {
    'product_name': ['LED', 'LCD', 'MOBILE', 'IRON'],
    'salesman_name': ['MOHAN', 'KEVIN', 'SUMIT', 'ARUN'],
    'price': [500, 400, 300, 125]
}
electronic1 = pd.DataFrame(data)

# Print the dataset (like PROC PRINT)
print("Electronic dataset of ABC online store (temporary):")
print(electronic1)

# Save as a permanent dataset (CSV file)
electronic1.to_csv('Electronic1.csv', index=False)

# Read the permanent dataset (simulating a permanent library)
libref_electronic1 = pd.read_csv('Electronic1.csv')

# Print the permanent dataset
print("\nElectronic dataset of ABC online store (permanent):")
print(libref_electronic1)

# Describe the structure of the dataset (like PROC CONTENTS)
print("\nStructure of the dataset:")
print(libref_electronic1.info())
print(libref_electronic1.describe(include='all'))

# Export a sample dataset (using seaborn's cars dataset as a substitute for sashelp.cars)
import seaborn as sns

cars = sns.load_dataset('mpg').dropna()  # 'mpg' is similar to 'cars'
cars.to_csv('cars.csv', index=False)
print("\nExported cars dataset to cars.csv")