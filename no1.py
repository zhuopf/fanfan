# coding:utf-8

"""小舞中午在饭堂吃饭,饭价是18.5元,买了一瓶可乐价格3.5元,吃了一份水果10.7元,请定义变量表示小舞在饭堂吃饭的花费,并计算总价格,在屏幕输出最终价格。"""

print("小舞吃饭的花销")
food_price = float(input("饭钱:"))
cola_price = float(input("可乐的价钱:"))
fruit_price = float(input("水果的价钱:"))

print("小舞吃饭的总价格:")
totalprice=food_price + cola_price + fruit_price
print(float(totalprice))