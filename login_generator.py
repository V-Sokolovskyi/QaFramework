import string
import secrets
def random_login(length_letters, length_digits):
    alphabet =string.ascii_letters 
    numbers = string.digits

    letters = ''.join(secrets.choice(alphabet) for _ in range(length_letters))
    digits = ''.join(secrets.choice(numbers) for _ in range(length_digits))
    login = letters + digits
    return login
    
