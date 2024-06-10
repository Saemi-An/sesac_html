class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f'Hi, my name is [{self.name}].')   # 객체의 매서드는 첫 번째 인자가 self여야 한다
        print(f'I am [{self.age}] years old.') 

    def walk(self):
        print(f'Hi, my name is [{self.name}].')   # 객체의 매서드는 첫 번째 인자가 self여야 한다
        print(f'I am [{self.age}] years old.') 


alice = Person('안새미',28)
alice.speak()

bob = Person('오송경',32)
bob.walk()
