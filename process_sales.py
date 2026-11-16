import csv
from pathlib import Path

# Define file locations
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "sales.csv"
OUTPUT_FILE = BASE_DIR / "output" / "processed_sales.csv"

# Read the raw sales data
with open(INPUT_FILE, "r", newline="") as file:
    reader = csv.DictReader(file)
    sales = list(reader)

# Calculate revenue for each order
for sale in sales:
    quantity = int(sale["quantity"])
    unit_price = float(sale["unit_price"])

    sale["total_revenue"] = round(quantity * unit_price, 2)

# Create output directory if it doesn't exist
OUTPUT_FILE.parent.mkdir(exist_ok=True)

# Save processed data
with open(OUTPUT_FILE, "w", newline="") as file:
    fieldnames = ["order_id", "product", "quantity",
                  "unit_price", "total_revenue"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(sales)

# Display summary
total_revenue = sum(sale["total_revenue"] for sale in sales)

print(f"Processed orders: {len(sales)}")
print(f"Total revenue: ${total_revenue:.2f}")