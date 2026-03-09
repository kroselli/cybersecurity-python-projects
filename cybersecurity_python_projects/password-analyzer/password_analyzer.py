import re

password = input("Enter a password to evaluate: ").strip()

length = len(password) >= 8
uppercase = bool(re.search(r"[A-Z]", password))
lowercase = bool(re.search(r"[a-z]", password))
digit = bool(re.search(r"[0-9]", password))
special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

score = sum([length, uppercase, lowercase, digit, special])

print("\nPassword Analysis:")
print(f"Length >= 8: {length}")
print(f"Contains uppercase letter: {uppercase}")
print(f"Contains lowercase letter: {lowercase}")
print(f"Contains digit: {digit}")
print(f"Contains special character: {special}")

if score == 5:
    print("\nResult: Strong password")
elif score >= 3:
    print("\nResult: Moderate password")
else:
    print("\nResult: Weak password")