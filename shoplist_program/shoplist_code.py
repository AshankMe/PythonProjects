print(" Prepare list of 3 items to shop")
shoplist =[] #creating empty list named shoplist
item1 = input("Enter first item")
shoplist.append(item1)
print(shoplist)
shoplist.append(item1)
item2 =input("Enter second item")
shoplist.append(item2)
item3 = input("Enter third item")
shoplist.append(item3)
print("The list prepared is ",shoplist)
print("Prepare list of items you shoped from above removing from shoplist and adding to new list say basket")
basket=[]
getitem1 = input("Enter one name you got from shop list items:")
shoplist.remove(getitem1)
basket.append(getitem1)
print("Shoplist",shoplist,len(shoplist),"items","\n basket",basket,len(basket),'items')
getitem2 = input("Enter one name except previously selected from items:")
shoplist.remove(getitem2)
basket.append(getitem2)
print("Shoplist",shoplist,len(shoplist),"items","\n basket",basket,len(basket),'items')
getitem3 = input("Enter one name except previously selected from items:")
shoplist.remove(getitem3)
basket.append(getitem3)
print("Shoplist",shoplist,len(shoplist),"items","\n basket",basket,len(basket),'items')