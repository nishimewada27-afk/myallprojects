import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # At least 8 characters
    if len(password) >= 8:
        strength += 1
    # At least one digit
    if re.search(r"\d", password):
        strength += 1
    # At least one uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    # At least one lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    # At least one special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength == 5:
        remarks = "Very Strong 💪"
    elif 3 <= strength < 5:
        remarks = "Medium 🙂"
    else:
        remarks = "Weak ⚠️"

    return remarks


# Example
pwd = input("Enter a password: ")
print("Password strength:", check_password_strength(pwd))
