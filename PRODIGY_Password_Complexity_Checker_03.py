import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 10:
        feedback.append("Good length (at least 10 characters).")
        score += 1
    else:
        feedback.append("Password should be at least 10 characters long.")

    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special characters (at least two)
    special_chars = re.findall(r'[@$!%*?&]', password)
    if len(special_chars) >= 2:
        score += 1
    else:
        feedback.append("Add at least two special characters (e.g., @, $, !, %, *, ?, &).")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    # Output results
    print("\n--- Password Strength Analysis ---")
    print(f"Password: {password}")
    print(f"Strength: {strength}\n")

    for f in feedback:
        print(f)

# --- Main Program ---
if __name__ == "__main__":
    print("=== Password Strength Checker ===")
    user_passwd = input("Enter your password: ")
    check_password_strength(user_passwd)
