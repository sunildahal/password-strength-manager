COMMON_PASSWORDS = [
    "password", "123456", "qwerty", "admin", "letmein",
    "welcome", "iloveyou", "monkey", "dragon"
]

def dictionary_attack(password):
    return password.lower() in COMMON_PASSWORDS
