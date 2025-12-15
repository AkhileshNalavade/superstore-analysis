import csv

data = [
    ["order_id","order_date","region","category","sub_category","sales","profit"],
    [1,"2024-01-05","South","Furniture","Chairs",5000,800],
    [2,"2024-01-07","East","Technology","Phones",15000,3000],
    [3,"2024-01-10","West","Office Supplies","Binders",2000,300],
    [4,"2024-02-02","South","Technology","Laptops",45000,7000],
    [5,"2024-02-05","North","Furniture","Tables",12000,-1500],
    [6,"2024-02-10","East","Technology","Phones",18000,3500],
    [7,"2024-03-01","West","Office Supplies","Paper",3000,400],
    [8,"2024-03-04","South","Furniture","Chairs",6000,900],
    [9,"2024-03-15","North","Technology","Accessories",5000,1200],
    [10,"2024-03-20","East","Office Supplies","Binders",2500,350]
]

with open("superstore.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("superztore.csv created successfully.")
