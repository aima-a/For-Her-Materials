''' Nested for loops: loop within a loop'''

regions = ["North", "South", "East", "West"]
products = ["Product A", "Product B", "Product C"]

total_sales = 0

for region in regions:  # Outer loop iterates through regions
    for product in products:    # Inner loop iterates through products; each combination is taken care of
        sales = float(input(f"Enter the sales for {product} in {region}: "))
        total_sales += sales

print("Total sales across all regions and products:", total_sales)