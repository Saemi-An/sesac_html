import random
city_names = ['Seoul', 'Hangkok', 'Hanoi', 'Shanghai', 'Tokyo', 'Osaka', 'Jeju', 'Gwang-Ju']


def generate_city():
        city_number = int(input('How many cities?: '))
        city_lst = []

        for _ in range(city_number):
            x = random.choice(city_names) 
            city_lst.append(x)   
        return print(city_lst)

generate_city()