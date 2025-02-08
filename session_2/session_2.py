import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {matplotlib.__version__}")

# Create a simple DataFrame with pandas
data = {
    "Stocks": ["AAPL", "JPM", "MSFT"],
    "Price": [150.75, 100.50, 200],
    "Shares": [10, 15, 25.5],
}
print(f"Data Dictionary: {data}")

df = pd.DataFrame(data)
print("\nSimple DataFrame:\n")
print(df)

# Use NumPy for numerical operations
prices = np.array([150.75, 152.30, 148.90, 151, 153.45, 164, 159.99])
print(f"Prices: {prices}")

average_price = np.mean(prices)
print(f"\nAverage stock price: ${average_price:.2f}")

price_sum = np.sum(prices)
print(f"Sum of stock prices: ${price_sum:.2f}")

price_min = np.min(prices)
print(f"Min stock prices: ${price_min:.2f}")

price_max = np.max(prices)
print(f"Max of stock prices: ${price_max:.2f}")

price_median = np.median(prices)
print(f"Median of stock prices: ${price_median:.2f}")

price_std_dev = np.std(prices)
print(f"Standard Deviation of stock prices: ${price_std_dev:.2f}")

# Plot with matplotlib
plt.figure(figsize=(8, 4))
plt.plot(prices, marker="o", linestyle=":", color="red")
plt.title("Stock Prices over time")
plt.xlabel("Time (artibitary units)")
plt.ylabel("Price")
plt.grid(True)
plt.show()

"""
## Mini "Hello Finance" Project: Simulate and Plot a Random Walk

Random Walk: Simple model for simulating stock price movement.
Assumption is that price changes are random and unpredicatable.
Read more about Random Walks here: [https://en.wikipedia.org/wiki/Random_walk](https://en.wikipedia.org/wiki/Random_walk)
"""

# Use seed - This ensures reproducibility, same random numbers each run
np.random.seed(42)  # If you want truly random numbers each run, remove this line
random_walk_no_sum = np.random.normal(0, 1, 250)
print(f"First 20 values of random_walk_no_sum:\n{random_walk_no_sum[0:20]}")

random_walk = np.random.normal(0, 1, 250).cumsum()
print(f"First 20 values of random_walk:\n{random_walk[0:20]}")

mean_walk_no_sum = np.mean(random_walk_no_sum)
std_walk_no_sum = np.std(random_walk_no_sum)
print(f"Mean of random walk_no_sum: {mean_walk_no_sum:.2f}")
print(f"Standard Deviation of random walk_no_sum: {std_walk_no_sum:.2f}")

mean_walk = np.mean(random_walk)
std_walk = np.std(random_walk)
print(f"Mean of random walk (Cumulative Sum): {mean_walk:.2f}")
print(f"Standard Deviation of random walk (Cumulative Sum): {std_walk:.2f}")

plt.figure(figsize=(20, 8))
plt.plot(random_walk, marker=".", linestyle="-", color="green")
plt.title("Simulated Random Walk (Stock Price Simulation)")
plt.xlabel("Time (days)")
plt.ylabel("Simulated Stock Price")
plt.grid(True)
plt.show()

plt.figure(figsize=(20, 8))
plt.plot(random_walk_no_sum, marker="o", linestyle="--", color="blue")
plt.title("Simulated Random Walk (No Cumulative Sum) #Wrong Plot")
plt.xlabel("Time (days)")
plt.ylabel("Simulated Stock Price")
plt.grid(True)
plt.show()

# Plot Normal Distribution vs Cumulative Sum of Normal Distributuon
plt.figure(figsize=(20, 8))
plt.plot(
    random_walk_no_sum,
    marker=".",
    linestyle="-",
    color="orange",
    label="Random Walk No CumSum",
)
plt.plot(
    random_walk,
    marker=".",
    linestyle="-",
    color="purple",
    label="Random Walk With Cumulative Sum",
)
plt.title("Random Walk No CumSum vs Random Walk With Cumulative Sum")
plt.xlabel("Time (days)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()