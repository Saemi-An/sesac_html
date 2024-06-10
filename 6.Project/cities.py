import random

city_names = ['Seoul', 'Hangkok', 'Hanoi', 'Shanghai', 'Tokyo', 'Osaka', 'Jeju', 'Gwang-Ju']

class GENERATE_CITY:

    def generate_city(self):
        city_number = int(input('How many cities?: '))
        city_lst = []

        for _ in range(city_number):
            x = random.choice(city_names) 
            city_lst.append(x)
        return city_lst   # city_lst = ['Hangkok', 'Osaka', 'Seoul', 'Jeju', 'Jeju']


    def save_city(self):
        f = open('cities.txt', 'w')
        f.write(self.generate_city())
        f.close()

saemi = GENERATE_CITY()

saemi.save_city()
