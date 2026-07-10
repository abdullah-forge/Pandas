import pandas as pd 
coffee = pd.read_csv("coffee_sales.csv")
coffee
coffee.head()
coffee.columns

# droping column 
coffee = coffee.drop("Discount", axis=1)
coffee.head()

# rename column
coffee = coffee.rename(columns={
    "Price_Per_Cup" : "Price"
})
coffee.head()

