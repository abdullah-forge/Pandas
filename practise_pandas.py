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
