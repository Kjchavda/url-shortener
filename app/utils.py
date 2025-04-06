import random
import string

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits  # a-zA-Z0-9
    return ''.join(random.choices(chars, k=length))