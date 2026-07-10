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

# creating new column and column multiplication
coffee["Total"] = coffee["Quantity"] * coffee["Price"]
coffee.head()

#save specific column 
customer_bill = coffee[["Customer", "Total"]]
customer_bill
customer_bill.to_csv("customer>bill.csv", index=False)

# merge
suppliers = pd.read_csv("coffee_suppliers.csv")
suppliers.head()
merge = pd.merge(
    coffee,suppliers, on="Coffee_Type"
)
merge
