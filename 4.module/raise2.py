
class CustomError(Exception):
    pass


def check_value(value):
    if value < 0 or value >= 100:
        raise CustomError('You should input between 1 to 99.')
    return value

result1 = check_value(30)
result2 = check_value(100)

print(result1)
print(result2)
