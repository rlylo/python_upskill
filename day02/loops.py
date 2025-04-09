"""
In Java
for(int i = 0; i <5; i++){
}
"""
from ftplib import print_line

for i in range(1,6):
    print(i)
    #print("Hello")


print("Hello World")

print("------------------------------------------")

s = "Selenium"

for x in s:
    print(x)

print("-------------------------")
reversed_string = ""
for i in s[::-1]:
    reversed_string += i
print(reversed_string)

print("--------------------------------------------")
for i in range(1,5):
    print(i)
    for j in range(1,3):
        print("Hello Selenium")

print("---------------------------------------------")

while True:
    print("While Loop")
    break

score = int(input("Enter your score: \n"))
while score>100 or score < 0:
    print("Score is invalid")
    score = int(input("Please re-enter score: \n"))
if score >= 0:
    print("Passed exam")
else:
    print("Failed exam")



