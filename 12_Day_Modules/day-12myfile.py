import random
import string

def random_user_id(length = 6):
    char_pool = string.ascii_letters + string.digits

    random_id = ''.join(random.choices(char_pool,k = length))

    return random_id
print(random_user_id())