price = int(input())
count = 0
coins = [500,100,50,10]

for coin in coins:
    coin_count = int(price / coin)
    price = price - coin_count * coin
    count = count + coin_count
print(count)