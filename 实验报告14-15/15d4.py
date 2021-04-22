class Item:
    def __init__(self,mark,color,price,**kwargs):
        self.mark = mark
        self.price=price
        self.color = color
    #def __str__(self):  # 重新输出
    # return "<Item {}>".format(self.mark)
    def __repr__(self):  # 重新输出
        return "<Item {}>".format(self.mark)
class Cart:   #购物车类
    def __init__(self):
        self.items=[]
    def additem(self,item:Item):
        self.items.append(item)
        return self
    def getall(self):
        return self.items

item1 = Item('牛奶','白色',200,weight= '4Kg')
item2 = Item('毛巾','黑色',10,size=14)

cart = Cart()
cart.additem(item1)
cart.additem(item2)
print(cart.getall()[0].__dict__)
for item in cart.getall():
    print(item)