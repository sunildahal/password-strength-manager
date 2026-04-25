def detect_patterns(password):
    patterns = []

    if password.isdigit():
        patterns.append("Only numbers")

    if password.isalpha():
        patterns.append("Only letters")

    if password.lower() in ["password", "qwerty", "admin", "letmein"]:
        patterns.append("Common weak password")

    if any(password[i] == password[i+1] for i in range(len(password)-1)):
        patterns.append("Repeated characters")

    keyboard_sequences = ["qwerty", "asdf", "zxcv"]
    for seq in keyboard_sequences:
        if seq in password.lower():
            patterns.append("Keyboard sequence detected")

    return patterns
