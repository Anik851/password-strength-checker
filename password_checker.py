import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    if score == 5:
        return "Strong Password", feedback
    elif score >= 3:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback


if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, suggestions = check_password_strength(password)

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions to improve:")
        for suggestion in suggestions:
            print("-", suggestion)
