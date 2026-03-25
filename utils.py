def is_even(number):
    return number % 2 == 0

def generate_password(length=8):
    import random
    import string
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
