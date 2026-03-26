# Input prices
prices = tuple(map(int, input("Enter item prices: ").split()))

print("Prices:", prices)

# a) Total items
print("Total items sold:", len(prices))

# b) Cheapest item
min_price = min(prices)
print("Cheapest item price:", min_price)

# c) Costliest item
max_price = max(prices)
print("Costliest item price:", max_price)

# d) Ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items
count_max = prices.count(max_price)
print("Number of costliest items sold:", count_max)
