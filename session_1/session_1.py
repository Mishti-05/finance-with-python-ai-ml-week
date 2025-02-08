stock_price = 150.75  # float
shares = 10  # int
stock_name = "AAPL"  # str
is_profitable = True  # boolean

print(f"stock_price: {stock_price} -> {type(stock_price)}")
print(f"shares: {shares} -> {type(shares)}")
print(f"stock_name: {stock_name} -> {type(stock_name)}")
print(f"is_profitable: {is_profitable} -> {type(is_profitable)}")

stock_prices = [150.75, 152.30, 148, 151.00, 153, "Closed-Sat", "Closed-Sun"]
print(f"stock_prices: {stock_prices}")
print(f"type(stock_prices): {type(stock_prices)}")
print(f"Length: {len(stock_prices)}")
print(f"stock_prices[6]: {stock_prices[6]}")

stock_info = {"name": "AAPL", "price": 150.75, "shares": 10}
print("stock_info:", stock_info)
print("type(stock_info):", type(stock_info))
print("stock_info['shares']:", stock_info["shares"])
print("stock_info.keys():", stock_info.keys())
print("stock_info.values():", stock_info.values())
print("stock_info.items():", stock_info.items())
print("stock_info.get('country'):", stock_info.get("country"))
print("stock_info.get('sector', 'Not Found'):", stock_info.get("sector", "Not Found"))


# Functions
def calculate_total_value(price, numOfShares):
    return price * numOfShares


total_value = calculate_total_value(stock_price, shares)
print(f"${total_value}")

total_value = calculate_total_value(1300, 16)
print(f"${total_value}")

# Control-Flow
print(f"total_value: {total_value}")
if total_value > 3000 and total_value < 5000:
    print("This is somewhat profitable")
elif total_value > 5000:
    print("This is very profitable")
else:
    print("This is NOT profitable")

# Loops
print(f"stock_prices: {stock_prices}")
for myPrice in stock_prices:
    if isinstance(myPrice, str):
        print(f"{myPrice}")
    else:
        print(f"${myPrice}")
