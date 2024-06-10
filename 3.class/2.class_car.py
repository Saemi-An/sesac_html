class Car:
    def __init__(self,brand,model,ordometer):
        self.brand = brand
        self.model = model
        self.ordometer = ordometer
    
    def get_name(self):
        print(f'{self.brand} - {self.model}')

    def get_ordormeter(self):
        print(f'{self.ordometer} droven.')

    def drive(self, mileage):
        def hello():
            return '3'

        x = self.ordometer =+ mileage
        y = format(x,',')
        print(f'You have droven {format(x,",")}km so far.')

my_car = Car('Hyundai','Genesis G70',0)
my_car.get_name()
my_car.get_ordormeter()
my_car.drive(60000)
