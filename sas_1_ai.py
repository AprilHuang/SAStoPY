import pandas as pd

# 1. Creating the data set in a temporary (in-memory) DataFrame
electronic1 = pd.DataFrame({
    'product_name': ['LED', 'LCD', 'MOBILE', 'IRON'],
    'salesman_name': ['MOHAN', 'KEVIN', 'SUMIT', 'ARUN'],
    'price': [500, 400, 300, 125]
})

print("Electronic dataset of ABC online store (temporary):")
print(electronic1)

# 2. Creating the data set in a 'permanent' way (e.g., saving to CSV)
electronic1.to_csv('Electronic1.csv', index=False)

# To simulate loading from a permanent store:
electronic1_perm = pd.read_csv('Electronic1.csv')
print("\nElectronic dataset of ABC online store (permanent):")
print(electronic1_perm)

# 3. Describes the structure of the data set (like PROC CONTENTS)
print("\nStructure of the Electronic1 dataset:")
print(electronic1_perm.info())

# 4. Exporting a sample DataFrame to CSV (simulating SASHELP.CARS export)
# Here, we use a pandas sample DataFrame for demonstration
cars = pd.DataFrame({
    'Make': ['Ford', 'Toyota', 'BMW'],
    'Model': ['F-150', 'Corolla', 'X5'],
    'Type': ['Truck', 'Sedan', 'SUV']
})
cars.to_csv('cars.csv', index=False)
print("\nExported cars.csv")