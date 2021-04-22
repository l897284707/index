# class Car:
#     _whil=4
#     def _drive(self):
#         print('xingshi')
#     def tes(self):
#         print(f"jiaocheyou {self._whil}")
#         self._drive()
# car=Car()
# print(car.tes())
class Gou():
    def __init__(self):
        self.color='lanse'
        print('chuangjian')
    def __del__(self):
        print('xiaohui')
car=Gou()
print(car.color)
del car
print(car.color)