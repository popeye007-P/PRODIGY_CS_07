import re


def check_password_strength(password):

    score = 0
    feedback = []

    if len(password) < 10:
        feedback.append(" Password should be at least 10 characters long.")
    else:
        feedback.append("Good Lengnth.")
        score += 1
    
    if not re.search(r'[A-Z]', password):                
        score += 1
    else:
        feedback.append("Add atleast one upper case letter.")
    
    if not re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add atleast one lower case letter.")
    
    if not re.search(r'[0-9]', password):
        score += 1
    else: 
        feedback.append("Add atleast one Number.")
    
    if not re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        feedback.append("Add atleast two special character (e.g., @, #, $, %).")

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
print("=== Password Strength Checker ===")
user_passwd = input("Enter your password: ")
check_password_strength(user_passwd)
