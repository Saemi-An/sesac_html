import random
import uuid

names = ['James', 'Lily', 'Akatuki', 'Saemi', 'Song', 'Zenda', 'Alice']

cities = ['New York', 'LA', 'Japan', 'Seoul', 'Paris', 'Hanburg', 'Düsseldorf']

def generate_name():
    return random.choice(names)

def generate_birthday():
    year = random.randint(1970, 2005)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f'{year}-{month:02d}-{day:02d}'

def generate_gender():
    return random.choice(['Male', 'Female'])

def generate_address():
    city = random.choice(cities)
    street = random.randint(1, 100)
    return f'{street} {city}'

data = []

for _ in range(10):
    name = generate_name()
    birthday = generate_birthday()
    gender = generate_gender()
    address = generate_address()
    a_user = (name, birthday, gender, address)
    data.append(a_user)

for d in data:
    print(d)
