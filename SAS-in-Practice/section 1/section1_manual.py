import pandas as pd
import seaborn as sns

electrionic_pd = pd.DataFrame({
    'product_name': ['LED', 'LCD', 'MOBILE', 'IRON'],
    'salesman_name': ['MOHAN', 'KEVIN', 'SUMIT', 'ARUN'],
    'price': [500, 400, 300, 125]
})

print("electronic dataset of ABC online store")
print(electrionic_pd)
print(electrionic_pd.info())

cars = sns.load_dataset('mpg').dropna()
cars.to_csv('cars.csv', index=False)