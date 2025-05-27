import pandas as pd

# Example: Load your data (replace with your actual file paths)
# salesmasterdata = pd.read_csv('salesmasterdata.csv')
# fashion = pd.read_csv('fashion.csv')
# ecommerce = pd.read_csv('ecommerce.csv')
# demo = pd.read_csv('demo.csv')
# electric = pd.read_csv('electric.csv')

# 1. List reports (PROC PRINT)
print(salesmasterdata[['custid', 'balance']])

# 2. Custom column headings
print(salesmasterdata[['custid', 'balance']].rename(
    columns={'custid': 'Customer ID', 'balance': 'Balance Amount'}
))

# 3. Reports by group (BY statement)
salesmasterdata_sorted = salesmasterdata.sort_values('gender')
for gender, group in salesmasterdata_sorted.groupby('gender'):
    print(f"\nGender: {gender}")
    print(group[['custid', 'balance', 'sales']])

# 4. Summing numeric variables by group
summary = salesmasterdata.groupby('gender')[['balance', 'sales']].sum()
print("\nTotal Balance and Sales by Gender:")
print(summary)

# 5. Customized layout with BY groups and ID variables
tempsales = salesmasterdata.sort_values(['gender', 'cardholder'])
for gender, group in tempsales.groupby('gender'):
    print(f"\nGender: {gender}")
    print(group[['cardholder', 'sales']])
    print("Total Sales:", group['sales'].sum())

# 6. Summary report (PROC MEANS)
means = fashion.groupby(['gender', 'fraudrisk'])['sales'].agg(['min', 'max', 'mean'])
print("\nSummary statistics for sales by gender and fraudrisk:")
print(means.round(3))

# 7. Frequency reports (PROC FREQ)
print("\nFrequency table: ship_mode")
print(ecommerce['ship_mode'].value_counts())
print("\nFrequency table: product")
print(ecommerce['product'].value_counts())

print("\nCross-tabulation: ship_mode x order_priority")
print(pd.crosstab(ecommerce['ship_mode'], ecommerce['order_priority'], margins=True, normalize=False))

# 8. PROC REPORT equivalent
demo['Incentive'] = demo['Sales'] * 0.1
print("\nSales Report:")
print(demo[['ORDID', 'Product', 'Sales', 'Incentive']])

# 9. ODS HTML/PDF/RTF/EXCEL reports (exporting to files)
electric_grouped = electric[electric['sales'] > 1400].groupby('gender')['sales'].sum().reset_index()
electric_grouped.to_html('Sales.html', index=False)
electric_grouped.to_csv('Sales.csv', index=False)
electric_grouped.to_excel('Sales.xlsx', index=False)
# For PDF/RTF, use libraries like matplotlib, reportlab, or docx as needed

# 10. List all pandas styles (not directly equivalent to SAS styles)
print("\nAvailable pandas styles: https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html")