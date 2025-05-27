import pandas as pd
import numpy as np
from io import StringIO

# Data set ADDRESS (multi-line records)
address_data = [
    ["ron   coDY", "1178  HIGHWAY 480", "camp   verde        tx 78010"],
    ["jason Tran", "123 lake  view drive", "East  Rockaway      ny 11518"]
]
address_records = []
for block in address_data:
    name = block[0].strip()
    street = block[1].strip()
    city_state_zip = block[2]
    city = city_state_zip[:20].strip()
    state = city_state_zip[20:22].strip()
    zip_code = city_state_zip[23:28].strip()
    address_records.append({
        "Name": name,
        "Street": street,
        "City": city,
        "State": state,
        "Zip": zip_code
    })
address = pd.DataFrame(address_records)

# Data set CHARS
chars = pd.DataFrame([
    ["58", "155", "10/21/1950"],
    ["63", "200", "5/6/2005"],
    ["45", "79", "11/12/2004"]
], columns=["Height", "Weight", "Date"])

# Data set CARELESS
careless = pd.DataFrame([
    [100, "COdY", "A", "b", "c"],
    [65, "sMITH", "C", "C", "d"],
    [95, "scerbo", "D", "e", "D"]
], columns=["Score", "Last_Name", "Ans1", "Ans2", "Ans3"])

# Data set CLEANING
cleaning = pd.DataFrame([
    ["Apple", "12345", "XYZ123"],
    ["Ice9", "123X", "Abc.123"],
    ["Help!", "999", "X1Y2Z3"]
], columns=["Letters", "Digits", "Both"])

# Data set ONEPER
oneper = pd.DataFrame([
    ["001", 450, 430, 410],
    ["002", 250, 240, np.nan],
    ["003", 410, 250, 500],
    ["004", 240, np.nan, np.nan]
], columns=["Subj", "Dx1", "Dx2", "Dx3"])

# Data set MANYPER (reshaped from ONEPER)
manyper = oneper.melt(id_vars=["Subj"], value_vars=["Dx1", "Dx2", "Dx3"],
                      var_name="Visit", value_name="Diagnosis")
manyper["Visit"] = manyper["Visit"].str.extract(r'(\d)').astype(int)
manyper = manyper.dropna(subset=["Diagnosis"]).sort_values(["Subj", "Visit"])

# Data set MONTH_DAY_YEAR
month_day_year = pd.DataFrame([
    [10, 21, 1950],
    [3, np.nan, 2005],
    [5, 7, 2000]
], columns=["Month", "Day", "Year"])

# Data set SALES (parsing $ and commas)
sales_data = StringIO("""\
1843 George Smith  North Barco_Corporation  10/10/2006 144L 50 $8.99
1843 George Smith  South Cost_Cutter's  10/11/2006 122 100 $5.99
1843 George Smith  North Minimart_Inc.  10/11/2006 188S 3 $5,199
1843 George Smith  North Barco_Corporation  10/15/2006 908X 1 $5,129
1843 George Smith  South Ely_Corp.  10/15/2006 122L 10 $29.95
0177 Glenda Johnson  East Food_Unlimited  9/1/2006 188X 100 $6.99
0177 Glenda Johnson  East Shop_and_Drop  9/2/2006 144L 100 $8.99
1843 George Smith  South Cost_Cutter's  10/18/2006 855W 1 $9,109
9888 Sharon Lu  West Cost_Cutter's  11/14/2006 122 50 $5.99
9888 Sharon Lu  West Pet's_are_Us  11/15/2006 100W 1000 $1.99
0017 Jason Nguyen  East Roger's_Spirits  11/15/2006 122L 500 $39.99
0017 Jason Nguyen  South Spirited_Spirits  12/22/2006 407XX 100 $19.95
0177 Glenda Johnson  North Minimart_Inc.  12/21/2006 777 5 $10.500
0177 Glenda Johnson  East Barco_Corporation  12/20/2006 733 2 $10,000
1843 George Smith  North Minimart_Inc.  11/19/2006 188S 3 $5,199
""")
sales = pd.read_csv(sales_data, sep=r'\s+', header=None, names=[
    "EmpID", "Name1", "Name2", "Region", "Customer", "Date", "Item", "Quantity", "UnitCost"])
sales["Name"] = sales["Name1"] + " " + sales["Name2"]
sales["UnitCost"] = sales["UnitCost"].replace(r'[\$,]', '', regex=True).astype(float)
sales["Quantity"] = sales["Quantity"].replace(r'[,]', '', regex=True).astype(float)
sales["TotalSales"] = sales["Quantity"] * sales["UnitCost"]
sales = sales[["EmpID", "Name", "Region", "Customer", "Date", "Item", "Quantity", "UnitCost", "TotalSales"]]

# Data set MEDICAL
medical = pd.DataFrame([
    ["001", "Mayo Clinic", "10/21/2006", 120, 78, "7", "Patient has had a persistent cough for 3 weeks."],
    ["003", "HMC", "9/1/2006", 166, 58, "8", "Patient placed on beta-blockers on 7/1/2006"],
    ["002", "Mayo Clinic", "10/01/2006", 210, 68, "9", "Patient has been on antibiotics for 10 days"],
    ["004", "HMC", "11/11/2006", 288, 88, "9", "Patient advised to lose some weight"],
    ["007", "Mayo Clinic", "5/1/2006", 180, 54, "7", "This patient is always under high stress"],
    ["050", "HMC", "7/6/2006", 199, 60, "123", "Refer this patient to mental health for evaluation"]
], columns=["Patno", "Clinic", "VisitDate", "Weight", "HR", "DX", "Comment"])

# Data set BICYCLES
bicycles = pd.DataFrame([
    ["USA", "Road Bike", "Trek", 5000, 2200],
    ["USA", "Road Bike", "Cannondale", 2000, 2100],
    ["USA", "Mountain Bike", "Trek", 6000, 1200],
    ["USA", "Mountain Bike", "Cannondale", 4000, 2700],
    ["USA", "Hybrid", "Trek", 4500, 650],
    ["France", "Road Bike", "Trek", 3400, 2500],
    ["France", "Road Bike", "Cannondale", 900, 3700],
    ["France", "Mountain Bike", "Trek", 5600, 1300],
    ["France", "Mountain Bike", "Cannondale", 800, 1899],
    ["France", "Hybrid", "Trek", 1100, 540],
    ["United Kingdom", "Road Bike", "Trek", 2444, 2100],
    ["United Kingdom", "Road Bike", "Cannondale", 1200, 2123],
    ["United Kingdom", "Hybrid", "Trek", 800, 490],
    ["United Kingdom", "Hybrid", "Cannondale", 500, 880],
    ["United Kingdom", "Mountain Bike", "Trek", 1211, 1121],
    ["Italy", "Hybrid", "Trek", 700, 690],
    ["Italy", "Road Bike", "Trek", 4500, 2890],
    ["Italy", "Mountain Bike", "Trek", 3400, 1877]
], columns=["Country", "Model", "Manuf", "Units", "UnitCost"])
bicycles["TotalSales"] = (bicycles["Units"] * bicycles["UnitCost"]) / 1000

# Data set ASSIGN (random group assignment)
np.random.seed(1357)
assign = pd.DataFrame({
    "Subject": np.arange(1, 37),
    "Group": np.random.rand(36)
})
assign["Rank"] = pd.qcut(assign["Group"], 3, labels=["A", "B", "C"])

# Data set DEMOGRAPHIC
demographic = pd.DataFrame([
    ["001", "10/15/1960", "M", "Friedman"],
    ["002", "8/1/1955", "M", "Stern"],
    ["003", "12/25/1988", "F", "McGoldrick"],
    ["005", "5/28/1949", "F", "Chien"]
], columns=["Subj", "DOB", "Gender", "Name"])

# Data set SOCIAL1 and SOCIAL2, and their cartesian product
social1 = pd.DataFrame({"SS1": ["123-45-6789", "001-34-9876", "007-77-6767", "102-43-9182"]})
social2 = pd.DataFrame({"SS2": ["123-45-6789", "001-43-9876", "007-77-6767", "485-46-1182", "102-43-9188"]})
social = social1.assign(key=1).merge(social2.assign(key=1), on='key').drop('key', axis=1)

# Data set SPSS
spss = pd.DataFrame([
    [68, 178, 55, 68, 210, "Smith"],
    [999, 200, 999, 999, 290, "Orlando"],
    [72, 999, 29, 79, 999, "Ramos"]
], columns=["Height", "Weight", "Age", "HR", "Chol", "Name"])

# Data set PERSONAL (multi-line, missover)
personal_blocks = [
    ["123-45-6789 M 0192M 11/15/1949", "Eggs Pancakes Sausage Toast Milk Coffee Beef Chicken"],
    ["013-54-9388 F 9981S 1/2/1981", "Pancakes Milk Chicken"],
    ["112-11-1309 M 1322M 03/29/1988", "Beef Toast Eggs Coffee"],
    ["778-44-4655 F 9899M 7/4/1981", "Pancakes Sausauge Coffee Beef"],
    ["445-45-4455 M 2938S 8/9/1977", "Tea Toast"]
]
personal_records = []
for block in personal_blocks:
    first = block[0].split()
    ss, gender, acctnum, dob = first[:4]
    foods = block[1].split() if len(block) > 1 else []
    foods = foods + [None] * (8 - len(foods))
    personal_records.append({
        "SS": ss, "Gender": gender, "AcctNum": acctnum, "DOB": pd.to_datetime(dob, format='%m/%d/%Y'),
        "Food1": foods[0], "Food2": foods[1], "Food3": foods[2], "Food4": foods[3],
        "Food5": foods[4], "Food6": foods[5], "Food7": foods[6], "Food8": foods[7]
    })
personal = pd.DataFrame(personal_records)

# ...continue for other datasets as needed...

# Example: print a few datasets
print("ADDRESS:\n", address)
print("\nCAREFUL:\n", careless)
print("\nSALES:\n", sales.head())
print("\nSPSS:\n", spss)
print("\nPERSONAL:\n", personal)
print("\nSOCIAL (cartesian product):\n", social.head())