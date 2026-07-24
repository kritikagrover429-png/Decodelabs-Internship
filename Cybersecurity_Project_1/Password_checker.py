import re
password = input("Enter your password: ")
score = 0
if len(password) >= 8:
    score += 1
else:
    print("❌ Password should be at least 8 characters long.")

if re.search(r"[A-Z]", password):
    score += 1
else:
    print("❌ Add at least one uppercase letter.")

if re.search(r"[a-z]", password):
    score += 1
else:
    print("❌ Add at least one lowercase letter.")

if re.search(r"[0-9]", password):
    score += 1
else:
    print("❌ Add at least one number.")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    print("❌ Add at least one special character.")

print("\nPassword Score:", score, "/5")

if score == 5:
    print("✅ Strong Password 💪")
elif score >= 3:
    print("🟡 Medium Password 👍")
else:
    print("🔴 Weak Password ❌")