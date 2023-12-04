import numpy as np
import pandas as pd


unfiltered_csv = pd.read_csv("/Users/erankatz/DataEngineeringProject/Crime_Data_from_2020_to_Present 2.csv")

area_df = unfiltered_csv[['AREA', 'AREA NAME', 'Rpt Dist No']]

crime_desc_df = unfiltered_csv[['Crm Cd', 'Crm Cd Desc']]

weapon_df = unfiltered_csv[['Weapon Used Cd', 'Weapon Desc']]

unfiltered_csv['VictId'] = unfiltered_csv.index

unfiltered_csv.to_csv("CrimeData.csv", index=False)

victim_df = unfiltered_csv[['VictId', 'Vict Age', 'Vict Sex', 'Vict Descent']]

case_details_df = unfiltered_csv[['DR_NO', 'DATE OCC', 'TIME OCC', 'Mocodes', 'LOCATION', 'LAT', 'LON']]
case_df = unfiltered_csv[['DR_NO', 'VictId', 'AREA', 'Crm Cd', 'Weapon Used Cd']]

area_df.to_csv("area.csv", index=False)
crime_desc_df.to_csv("crime_description.csv", index=False)
weapon_df.to_csv("weapon.csv", index=False)
victim_df.to_csv("victim.csv", index=False)
case_details_df.to_csv("case_details.csv", index=False)
case_df.to_csv("case.csv", index=False)
