denon=[1,2,5,10,20,50]
price=38
while price>0:
    coin=int(input("insert a coin "))
    if coin == 0:
        print("thank you for shopping")
        break
    if coin in denon:
        if coin<=price:
            price = price - coin
            print("Due amount :",price)
        else:
            coin=coin-price
            print("plz take your coke and get your",coin ,"rupees")
            break
    else:
        print("plz insert a valid coin")
if price==0:
    print("plz take your product ")
    
