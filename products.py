products = []
while True:
	 name = input ('請輸入商品名稱:')
	 if name == 'q': #逃出迴圈
	 		break
	 price = input ('請輸入價格:')
	 p = [] # p = [nema, price]
	 p.append(name)
	 p.append(price)
	 products.append(p)# append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])