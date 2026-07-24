import re

print("===== PHISHING AWARENESS ANALYZER =====")

message = input("\nPaste Email or Message:\n")

red_flags = []

keywords = [
    "urgent",
    "verify",
    "password",
    "bank",
    "account",
    "click",
    "login",
    "winner",
    "free",
    "gift",
    "claim",
    "limited time",
    "otp"
]

for word in keywords:
    if word.lower() in message.lower():
        red_flags.append(f"Suspicious keyword found: {word}")

urls = re.findall(r'https?://\S+|www\.\S+', message)

for url in urls:
    red_flags.append(f"Suspicious Link Found: {url}")

print("\n========== RESULT ==========")

if red_flags:
    print("\n⚠ Possible Phishing Message\n")

    print("Red Flags:")
    for flag in red_flags:
        print("-", flag)

    print("\nReason:")
    print("This message contains phishing indicators.")
    print("Do not click links or share personal information.")

else:
    print("\nSafe Message")
    print("No phishing indicators found.")