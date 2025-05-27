import pandas as pd

# Load your data (replace with actual loading code)
# electric = pd.read_csv('electric.csv')

data = {
    "idx": list(range(1, 11)),
    "gender": [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    "sales": [1200, 1800, 1500, 2100, 1700, 1600, 2000, 1900, 1550, 1750],
    "balance": [15000, 7000, 6000, 8000, 7500, 7200, 9000, 18500, 6800, 7900]
}

electric = pd.DataFrame(data)
# 1. Select gender and sales
#print(electric[['gender', 'sales']])


# 2. Apply condition using where and group by
salesnumber = electric[electric['sales'] > 1400].groupby('gender')['sales'].sum().reset_index(name='salesnumber')
#print(salesnumber)

# 3. Having condition: oldest cust of each gender (max sales per gender)
idx = electric.groupby('gender')['sales'].idxmax()
oldest_cust = electric.loc[idx]
#print(oldest_cust)

# 4. Sorting based on ascending
asc_sorted = electric[electric['sales'] > 1500][['gender', 'sales']].sort_values('sales')
#print(asc_sorted)

# 5. Sorting based on descending
desc_sorted = electric[electric['sales'] > 1500][['gender', 'sales']].sort_values('sales', ascending=False)
#print(desc_sorted)

# 6. Creating a new table with bonus column
newtable = electric[electric['sales'] > 1500][['gender', 'sales']].copy()
newtable['bonus'] = newtable['sales'] * 0.5
newtable = newtable.sort_values('sales', ascending=False)
#print(newtable)

# 7. Print where gender == 1, with dynamic title (simulate macro variables)
from datetime import datetime
now = datetime.now()
print(f"status of sales order as {now.strftime('%A %d%b%Y %H:%M:%S')}")
print(electric[electric['gender'] == 1])

# 8. User-defined macro variable equivalent
gender_type = 2
print(f"status of sales order as {now.strftime('%A %d%b%Y %H:%M:%S')}")
print(electric[electric['gender'] == gender_type])

# 9. Macro-like function for balance threshold
def test(demo):
    print(electric[electric['balance'] > demo])

test(10000)

# 10. Macro functions with PROC MEAN equivalent
var1, var2 = 'sales', 'balance'
print(f"{var1.upper()} and {var2.upper()} for {electric.__class__.__name__.upper()} channel")
means = electric.groupby('gender')[[var1, var2]].mean()
print(means)