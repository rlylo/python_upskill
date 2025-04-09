n = "Automation Testing"

print(n[0])
print(n[-1])
print(len(n))
print(n[len(n) - 1])
n = n.lower()
print(n)

print("----------------------------------------------------")

s = "Python programming Language"
s1 = s[7:]
print(s1)
s2 = s[:18]
print(s2)
reversedString = s[::-1]
print(reversedString)
s3 = str(reversed(reversedString))
print(s3)

print("--------------------------------------------------")

expected_title = "cydeo"
actual_title = "CYDEO"
print(expected_title.lower() == actual_title.lower())


