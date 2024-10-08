def get_sales_data():
    sales_data = []
    while True:
        product_name = input("Enter product name (or type 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        category = input("Enter category: ")
        units_sold = int(input("Enter units sold: "))
        unit_price = float(input("Enter unit price: "))
        sales_data.append({
            "product_name": product_name,
            "category": category,
            "units_sold": units_sold,
            "unit_price": unit_price
        })
    return sales_data

def analyze_sales_data(sales_data):
    total_sales = 0
    total_units_sold = 0
    category_sales = {}
    product_sales = {}

    for item in sales_data:
        product_name = item["product_name"]
        category = item["category"]
        units_sold = item["units_sold"]
        unit_price = item["unit_price"]
        sales = units_sold * unit_price
        total_sales += sales
        total_units_sold += units_sold
        product_sales[product_name] = sales
        if category not in category_sales:
            category_sales[category] = 0
        category_sales[category] += sales

    average_sales_per_product = total_sales / len(sales_data) if sales_data else 0
    top_selling_product = max(product_sales, key=product_sales.get) if product_sales else None

    print(f"\nTotal Sales: {total_sales:.2f}")
    print(f"Average Sales per Product: {average_sales_per_product:.2f}")
    
    if top_selling_product:
        print(f"Top-Selling Product: {top_selling_product} ({product_sales[top_selling_product]:.2f})")

    print("\nSales by Category:")
    for category, sales in category_sales.items():
        print(f"{category}: {sales:.2f}")

def main():
    print("Enter sales data for each product. Type 'done' when you are finished.")
    sales_data = get_sales_data()
    if sales_data:
        analyze_sales_data(sales_data)
    else:
        print("No sales data was entered.")

if __name__ == "__main__":
    main()
