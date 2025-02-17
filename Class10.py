

try:
    user = int(unput("Enter your number"))
        for i in range(1,11):
            print(f"{user} x {i} = {user * i}")
except Exception as error:
    print(error)