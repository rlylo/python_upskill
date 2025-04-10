browsers = ("Chrome", "Safari", "Firefox", "Edge")

print(browsers)
print(type(browsers))
print(len(browsers))

print(browsers[1])
print(browsers[-1])

a1 = browsers[:3]
print(a1)
a2 = browsers[1:3]
print(a2)
print(type(a2))

reversed_tuple = browsers[::-1]
print(reversed_tuple)

result = tuple(reversed(browsers))
print(browsers)
print("+++")
print(result)

for each in browsers:
    print(each)

print("-------------------------------------------")
# browsers[1] = "Cydeo"
# print(browsers)

print("-------------------------------------------")
group_scores = ((70, 65, 80), (55, 85, 70), (68, 78, 48))
print(group_scores)

for i in group_scores:
    for j in i:
        print(j)

print("----------------------------------------------")

t1 = (1, 2, 3, 4, 5)
t2 = (6, 7, 8, 9, 10, 11, 12)
t3 = (13, 14, 15, 16)
merged_tuples = t1 + t2 + t3
print(merged_tuples)