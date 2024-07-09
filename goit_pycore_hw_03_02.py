import random

def get_numbers_ticket(min : int, max : int, quantity : int):
    try:
        if min < 1 or max > 1000 or max < min or quantity > max - min + 1:
            print("Incorrect input parameters.")
            return []
        else:
            numbers = list(range(min, max + 1))
            sample = sorted(random.sample(numbers, quantity))
            #sample.sort()
            return sample
    except TypeError:
        print("All input parameters must be positive integers.")
        return []


result = get_numbers_ticket(1,10,5)
print(result)
result = get_numbers_ticket(5,15,4)
print(result)
result = get_numbers_ticket(3,9,10)
print(result)
result = get_numbers_ticket(1,20,"25")
print(result)