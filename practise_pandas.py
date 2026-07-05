#1
import pandas as pd
import numpy as np
df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
    columns=["A", "B", "C"],
    index=["x", "y", "z", "zz"]
)
df.head()
df.tail

#2
olympics_data = pd.read_csv("bios.csv")
olympics_data.columns
olympics_data.loc[0]
# slicing 
olympics_data.loc[0: 4]

#3
olympics_data.iloc[0:5,[0,2]]
for index, row in olympics_data.iterrows():
  print(index)
  print(row['Born'])

#4
#Filtering Data
olympics_data.loc[olympics_data['Born'] == '1924']
olympics_data.loc[(olympics_data['Born'] == '1924') & (olympics_data['Sex'] == 'Male')]
olympics_data['Died_Year'] = pd.to_numeric(olympics_data['Died'].str.extract('(\d{4})')[0], errors='coerce')

# Filtering using the new numeric column
result = olympics_data.loc[(olympics_data['Original name'] == 'Keith') & (olympics_data['Died_Year'] <= 2020)]
result
olympics_data[olympics_data['Original name'].str.contains("Keith", case=False, na=False)]
