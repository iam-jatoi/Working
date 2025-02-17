#If, else, elif


#if Condition
num1: int = 100
if num > 10 and num1 < 100:
    print("Condion is True")


#if else Condition
name: str = "Sir Aneeq"
if name == "Sir Aneeq":
    print("Welcome Sir Aneeq")
else:
    print("Aap kon")


num1: int = 20
if num1 > 20:
    print("Condition is Positive")
else:
    print("Condition is Negative")



#if else elif condition
time_of_day: str = "Morning"

if time_of_day == "Evening":
    print("Good Evening")
elif time_of_day == "Afternoon":
    print("Goof Afternoon")
elif time_of_day == "Morning":
    print("Good Morning")
else:
    print("Good Night")



#if ki condition ki sirf Eik hi hoti hy
time_of_day: str = "abc"

if time_of_day == "Evening": #Agar if ki condition to True huwi to Result True Aajyega warna elif pe jayega
    print("Good Evening")
elif time_of_day == "Afternoon":
    print("Goof Afternoon")
elif time_of_day == "Morning":  
    print("Good Morning")
else:                       #Agar sab ki condition False huwi to Final result Else ki Aayegi
    print("Good Night")


#Data Type
#str, int, bool, list

#index      0,     1,       2,      3
names = ["Apple","Banana","Mango"."Guava"]
print(names)
print(names[1])

numbers = [1,2,3,4,5]
print(numbers[0]) 
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

for num in numbers:
    print(num)


#
#
# condition
# increment

# print(range(1,5))
# print(*range(1,5))



# for Loop => it means Repeatation
# iterables = is pe chalta hy 