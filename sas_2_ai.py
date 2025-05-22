import pandas as pd

## 1 Print Datasets (Equivalent to proc print)
# Replace with your actual file paths or data sources
electric = pd.read_csv('electric.csv')    # or pd.read_excel('electric.xlsx')
fashion = pd.read_csv('fashion.csv')

print(electric)
print(fashion)

## 2 Concatenate Two Datasets with Same Variables
concatenateset = pd.concat([electric, fashion], ignore_index=True)

## 3 Concatenate Datasets with Different Variables
from datetime import datetime

admindept = pd.DataFrame({
    'empid': [1, 3, 6],
    'name': ['Rick', 'Mike', 'Tusar'],
    'salary': [623.3, 611.5, 578.6],
    'DOJ': [datetime.strptime(d, '%d%b%Y') for d in ['02APR2001', '21OCT2000', '01MAR2009']]
})

financedept = pd.DataFrame({
    'empid': [2, 4, 7],
    'name': ['Andy', 'Rusell', 'John'],
    'salary': [567.2, 683.2, 594.5]
})

combineset = pd.concat([admindept, financedept], ignore_index=True, sort=False)

## 4 Append Datasets (PROC APPEND Equivalent)
# Append financedept to admindept (adds rows, aligns columns)
admindept_appended = pd.concat([admindept, financedept], ignore_index=True, sort=False)
print(admindept_appended)

# Append admindept to financedept
financedept_appended = pd.concat([financedept, admindept], ignore_index=True, sort=False)
print(financedept_appended)

# Assuming 'custID' exists in both datasets
fashion_sorted = fashion.sort_values(by='custID')
electric_sorted = electric.sort_values(by='custID')

interleavedata = pd.concat([fashion_sorted, electric_sorted], ignore_index=True).sort_values(by='custID')

## 5 Interleaving by Sorting
# Assuming 'custID' exists in both datasets
fashion_sorted = fashion.sort_values(by='custID')
electric_sorted = electric.sort_values(by='custID')

interleavedata = pd.concat([fashion_sorted, electric_sorted], ignore_index=True).sort_values(by='custID')

## 6 One-to-One Reading (Row-wise Combine)
customer = pd.DataFrame({
    'orderid': [1, 2, 3, 4, 5],
    'sales': [5000, 6000, 4000, 8000, 7000],
    'product': ['Camera', 'TV', 'Fridge', 'Laptop', 'Desktop']
})

sales = pd.DataFrame({
    'orderid': [1, 2, 3, 4, 5, 6],
    'customername': ['Mike', 'Rusell', 'Adam', 'Gary', 'Steve', 'Craig'],
    'pincode': [560035, 560045, 560078, 560075, 560076, 560035]
})

# One-to-one reading: combine row-wise by index (like SAS SET with two datasets)
onetoonereadset = pd.concat([customer, sales], axis=1)