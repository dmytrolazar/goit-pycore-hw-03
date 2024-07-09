import re

def normalize_phone(phone_number):
    try:
        phone_number = re.sub(r"\D", "", phone_number) # delete all non-digit character
        phone_number = re.sub(r"^0", "380", phone_number) # add country code if missing
        phone_number = re.sub(r"^380", "+380", phone_number) # add '+'
        return phone_number
    except TypeError:
        print("Input parameter must be a string.")

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
correct_result = ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
print("Expected output: ", correct_result)
print("My output:       ", sanitized_numbers)

# Check if the lists are identical
result = all(x == y for x, y in zip(sanitized_numbers, correct_result))
 
# Print the result
print("The lists are identical:", result)