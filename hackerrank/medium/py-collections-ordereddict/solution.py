# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

ord_dic = OrderedDict()
for _ in range(int(input())):
    product_name,price = input().rsplit(" ",1)
    ord_dic[product_name] = ord_dic.setdefault(product_name, 0) + int(price)
for key , value in ord_dic.items():
    print(f"{key} {value}")
