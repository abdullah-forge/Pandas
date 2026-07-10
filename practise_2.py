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

branches = pd.read_csv("coffee_branches.csv")
coffee_branches = pd.merge(
    coffee, branches, on="City"
)
coffee_branches

new_orders = pd.read_csv("new_orders.csv")
#concatenating
all_orders = pd.concat([coffee, new_orders], ignore_index = True)
all_orders
# combine
combined = coffee.join(branches.set_index("City"), on="City")
combined

combined.to_csv("final_coffee_data.csv",index=False)

quantity = coffee.loc[0,"Quantity"]
if quantity > 2:
  print("Large Order")
else:
  print("Small order")


#using for loop
for qty in coffee["Quantity"]:
  if qty > 3:
    print("Bulk Order")
  else:
    print("Small Order")
