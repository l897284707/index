class Person(object):
    def say_hello(self):
        print('打招呼')
class Chinese(Person):
    def say_hello(self):
        super().say_hello()
        print('吃了吗')
chinese=Chinese()
chinese.say_hello()