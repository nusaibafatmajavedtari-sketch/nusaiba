print("AN ARMSTRONG NUMBER CHECKER")

num = input("Enter a number: ")
digit_count = len(num)
print(f"Number of digits: {digit_count}")
total = 0

for digit in num:
    power = int(digit)**digit_count
    print(f"{digit} to the power {digit_count} = {power}")
    total += power

print(f"Sum of the powers = {total}")
if total == int(num):
    print(f"{num} is an armstrong number")
else: print(f"{num} is not an armstrong number")