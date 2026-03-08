import random
import string

def random_user_id(length):
    char_pool = string.ascii_letters + string.digits

    random_id = ''.join(random.choices(char_pool,k = length))

    return random_id
print(random_user_id(6))

def new_random_user_id(length,i):
    char_pool = string.ascii_letters + string.digits
    for s in range(i):
        random_id = ''.join(random.choices(char_pool,k = length))
        print(random_id)

new_random_user_id(16,3)

def rgb():

    color_values = [str(random.randint(0, 255)) for _ in range(3)]
    
    return ','.join(color_values)

print(rgb())

def generate_colors(st,i):

    color_values = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(i)]

    return ','.join(color_values)

print(generate_colors('hex',3))
