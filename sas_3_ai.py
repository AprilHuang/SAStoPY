import pandas as pd

# Example electric DataFrame (replace with actual data loading)
electric = pd.DataFrame({
    "custID": range(1, 11),
    "cardholder": [f"CH{i}" for i in range(1, 11)],
    "gender": [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    "sales": [1000, 1300, 1500, 900, 2000, 1100, 1700, 800, 2100, 1200],
    "balance": [10000, 15000, 9000, 13000, 8000, 14000, 7000, 16000, 6000, 17000]
})

# 1. Delete observations where sales < 1500
delete_final = electric[electric['sales'] >= 1500]
print("delete_final:\n", delete_final)

# 2. Drop variables
drop_set = electric.drop(columns=['cardholder', 'gender'])
print("\ndrop_set:\n", drop_set)

drop_set2 = electric.drop(columns=['cardholder', 'gender'])
print("\ndrop_set2:\n", drop_set2)

# 3. Keep variables
keep_set = electric[['cardholder', 'gender']]
print("\nkeep_set:\n", keep_set)

keep_set2 = electric[['cardholder', 'gender']]
print("\nkeep_set2:\n", keep_set2)

# 4. DO END LOOP: multiples of 5 up to 100
multiply = pd.DataFrame({'multiple': [i*5 for i in range(1, 21)]})
print("\nmultiply:\n", multiply)

# 5. DO UNTIL LOOP: multiples of 5 up to 100
multiple = 0
lst = []
while multiple < 100:
    multiple += 5
    lst.append(multiple)
multiply1 = pd.DataFrame({'multiple': lst})
print("\nmultiply1 (do until):\n", multiply1)

# 6. DO WHILE LOOP: multiples of 5 up to 100
multiple = 0
lst = []
while multiple < 100:
    multiple += 5
    lst.append(multiple)
multiply1_while = pd.DataFrame({'multiple': lst})
print("\nmultiply1 (do while):\n", multiply1_while)

# 7. Rename variables
rename_set = electric.rename(columns={'cardholder': 'card_owner', 'gender': 'gender_type'})
print("\nrename_set:\n", rename_set)

# 8. Label (not directly supported in pandas, but can use .rename for display)
rename_set_label = electric.rename(columns={'cardholder': 'card_owner', 'gender': 'gender_type'})
rename_set_label = rename_set_label.rename(columns={'custID': 'customer_id'})
print("\nrename_set with label:\n", rename_set_label)

# 9. Format sales as currency (display only)
format_set = rename_set.copy()
format_set['sales'] = format_set['sales'].apply(lambda x: "${:,.3f}".format(x))
print("\nformat_set (sales formatted):\n", format_set)

# 10. Format name to uppercase
admindept = pd.DataFrame({
    'empid': [1, 3, 6],
    'name': ['Rick', 'Mike', 'Tusar'],
    'salary': [623.3, 611.5, 578.6],
    'DOJ': ['02APR2001', '21OCT2000', '01MAR2009']
})
format_set2 = admindept.copy()
format_set2['name'] = format_set2['name'].str.upper()
print("\nformat_set2 (name uppercase):\n", format_set2)

# 11. Define length of variable (not needed in pandas, but can pad/truncate)
sales_test = pd.DataFrame({'Salesperson': ['Alice', 'Bob', 'Charlie']})
sales_test['Salesperson'] = sales_test['Salesperson'].str[:20]
print("\nsales_test:\n", sales_test)

# 12. BY statement to aggregate subgroups (Annual Payroll by Department)
salaries = pd.DataFrame({
    'Department': ['BAD', 'BAD', 'BAD', 'BAD', 'BAD', 'DDG', 'DDG', 'PPD', 'PPD', 'PPD', 'STD', 'STD'],
    'Name': ['Carol', 'Elizabeth', 'Linda', 'Thomas', 'Lynne', 'Jason', 'Paul', 'Kevin', 'Amber', 'Tina', 'Helen', 'Jim'],
    'WageCategory': ['Salaried', 'Salaried', 'Salaried', 'Salaried', 'Hourly', 'Hourly', 'Salaried', 'Salaried', 'Hourly', 'Salaried', 'Hourly', 'Salaried'],
    'WageRate': [20000, 5000, 7000, 9000, 230, 200, 4000, 5500, 150, 13000, 200, 8000]
})

def compute_payroll(df):
    df = df.copy()
    df['YearlyWage'] = np.where(df['WageCategory'] == 'Salaried', df['WageRate']*12, df['WageRate']*2000)
    payroll = df.groupby('Department')['YearlyWage'].sum().reset_index()
    payroll = payroll.rename(columns={'YearlyWage': 'Payroll'})
    payroll['Payroll'] = payroll['Payroll'].apply(lambda x: "${:,.0f}".format(x))
    return payroll

budget = compute_payroll(salaries)
print("\nAnnual Payroll by Department:\n", budget)

# 13. SORT PROCEDURE - ascending
sort_set = electric.sort_values('balance')
print("\nsort_set (ascending balance):\n", sort_set)

# 14. SORT PROCEDURE - descending
sort_set_desc = electric.sort_values('balance', ascending=False)
print("\nsort_set_desc (descending balance):\n", sort_set_desc)

# 15. SORT original dataset by sales
electric = electric.sort_values('sales')
print("\nelectric sorted by sales:\n", electric)