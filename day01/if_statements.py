from importlib.util import source_hash

browser_name = "firefox"

if browser_name == "chrome":
    print("chrome browser is selected")
    print("Opening Chrome browser")
elif browser_name == "firefox":
    print("Firefox browser is selected")
    print("Opening Chrome browser")
else:
    print("Safari browser is selected")
    print("Opening Chrome browser")

print("---------------------------------------------------------------")

score = 60

if 0 <= score <= 100:
    if score >= 60:
        print("Passed")
    else:
        print("Failed")

else:
    print("Incorrect score")

print("----------------------------------------------------")
if True:
    pass
else:
    pass

def function_name():
    pass

class Animal:
    pass

print("-----------------------------------------------------")
name = input("Enter name")
print(name)
