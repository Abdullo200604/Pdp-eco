def gnom():
    coins = list(map(int, input().split()))
    price = int(input())

    total_coins = sum(coins)

    if total_coins >= price:
        print(0)
    else:
        print(price - total_coins)

gnom()