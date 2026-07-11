import pandas as pd
coffee = pd.read_csv("coffee_sales.csv")
coffee.head()
coffee.info()
coffee.shape
coffee.describe()
coffee.columns

#Create Some Null Values
coffee.loc[2,"Quantity"] = None
coffee.loc[5,"Price_Per_Cup"] = None
coffee.loc[7, "City"] = None
coffee

#Handling Null Values
coffee.isna()
coffee.isna().sum()
coffee.notna()
coffee.fillna(0)
coffee["Quantity"] = coffee["Quantity"].fillna(coffee["Quantity"].mean())

coffee.dropna()
coffee["Quantity"] = coffee["Quantity"].interpolate()

#Aggregate Functions
coffee["Quantity"].sum()
coffee["Price_Per_Cup"].mean()
coffee["Price_Per_Cup"].max()
coffee["Price_Per_Cup"].min()

#value_counts
coffee["Coffee_Type"].value_counts()
coffee["City"].value_counts()

