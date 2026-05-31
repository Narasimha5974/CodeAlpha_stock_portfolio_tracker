# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGL": 140
}

# Dictionary to store user portfolio
portfolio = {}

# Input loop
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")

# Calculate total investment
total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares → ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to file
save_choice = input("Do you want to save results to a file? (y/n): ").lower()
if save_choice == "y":
    file_type = input("Save as .txt or .csv? ").lower()
    filename = f"portfolio.{file_type}"
    if file_type == "txt":
        with open(filename, "w") as f:
            f.write("Your Portfolio:\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares → ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value: ${total_value}\n")
    elif file_type == "csv":
        import csv
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock] * qty])
            writer.writerow(["Total", "", total_value])
    print(f"Portfolio saved to {filename}")
