N = int(input())
distances = list(map(int, input().split()))
oil_prices = list(map(int, input().split()))

min_price = oil_prices[0]
result = oil_prices[0] * distances[0]

for i in range(1, N-1) :
    if min_price > oil_prices[i]:
        min_price = oil_prices[i]
    result += min_price * distances[i]

print(result)
