import requests
import pandas as pd

# 1. Download the Excel file
url = "https://www2.census.gov/programs-surveys/decennial/2020/data/apportionment/apportionment-2020-table01.xlsx"
excel_path = "apportionment-2020-table01.xlsx"
with requests.get(url, stream=True, verify=False) as r:
    r.raise_for_status()
    with open(excel_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# 2. Read the relevant range from the Excel file
df = pd.read_excel(
    excel_path,
    sheet_name="Table 1",
    usecols="A:D",
    skiprows=3,
    nrows=51,  # 50 states + DC, adjust if needed
    engine="openpyxl"
)
print(df.columns)
# 3. Rename columns to match SAS output
df = df.rename(columns={
    "STATE": "state_name",
    df.columns[1]: "APPORTIONMENT POPULATION \n(APRIL 1, 2020)",
    "NUMBER OF APPORTIONED REPRESENTATIVES BASED ON \n2020 CENSUS2": "reps",
    "CHANGE FROM \n2010 CENSUS APPORTIONMENT": "change_reps"
})

# 4. Merge in 2-character state codes
# You can use a built-in pandas dataset or create your own mapping
us_state_abbrev = pd.read_csv(
    "https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv"
)
us_state_abbrev = us_state_abbrev.rename(columns={"State": "state_name", "Abbreviation": "statecode"})
df = df.merge(us_state_abbrev, on="state_name", how="left")

# 5. Create labels for states with change_reps != 0
labels = df[df["change_reps"] != 0].copy()
labels["change_reps_text"] = labels["change_reps"].apply(lambda x: f"+{x}" if x > 0 else str(x))

# 6. (Optional) Map plotting using Plotly
import plotly.express as px

fig = px.choropleth(
    df,
    locations="statecode",
    locationmode="USA-states",
    color="change_reps",
    hover_name="state_name",
    hover_data=["reps", "change_reps"],
    color_continuous_scale=["white", "#fdbf6f", "#b2df8a", "#33a02c"],
    scope="usa",
    labels={"change_reps": "Change in Reps"}
)
fig.update_layout(
    title_text="State Apportionment Changes based on 2020 Census",
    geo=dict(showlakes=True, lakecolor="LightBlue"),
)
fig.show()

# 7. (Optional) Add text labels for states with change_reps != 0
# Plotly does not support direct text overlay on choropleth, but you can use go.Scattergeo for advanced overlays.

# 8. Save processed data if needed
df.to_csv("census_apportionment_processed.csv", index=False)