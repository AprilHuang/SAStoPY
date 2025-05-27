import pandas as pd
import numpy as np

# Example electric DataFrame (replace with actual data loading)
electric = pd.DataFrame({
    "custID": range(1, 11),
    "sales": [1000, 1300, 1500, 900, 2000, 1100, 1700, 800, 2100, 1200],
    "balance": [10000, 15000, 9000, 13000, 8000, 14000, 7000, 16000, 6000, 17000]
})

# LOGIC ERRORS: Write custom messages and delete rows
def warn_and_filter(df):
    mask = df['balance'] < 12000
    for idx, row in df[mask].iterrows():
        print(f"MY_WARNING: The balance is too low: {row['custID']} balance= {row['balance']}.")
        print("MY_WARNING: customer deleted from temp dataset.\n")
    return df[~mask]

temp = warn_and_filter(electric)

# To write the current contents of the dataset or values of all variables
print("\nCurrent contents of temp dataset:")
print(temp)

# _N_ and _ERROR_ equivalent
def bonus_or_error(df):
    for i, row in df.iterrows():
        if row['sales'] > 1200:
            bonus = row['sales'] * 0.5
            print(f"Row {i+1}: sales={row['sales']}, bonus={bonus}")
        else:
            print(f"DATA ERROR : sales = {row['sales']} _n_ = {i+1}")

bonus_or_error(electric)

# DATA ERROR - Invalid Data
# Simulate reading data with invalid salary values
emp_data = [
    {"emp_id": 1, "name": "jack", "salary": "250o0"},
    {"emp_id": 2, "name": "kim", "salary": "29000"},
    {"emp_id": 3, "name": "sam", "salary": "43000"},
    {"emp_id": 4, "name": "rick", "salary": "56o756"},
    {"emp_id": 5, "name": "Tom", "salary": "456789"},
]
emp = pd.DataFrame(emp_data)

# Try to convert salary to numeric, set errors='coerce' to handle invalid entries
emp['salary'] = pd.to_numeric(emp['salary'], errors='coerce')

print("\nEmployee Data (with invalid salary handled as NaN):")
print(emp)