# Default Function
# Default Parameter wo hoty hen jo Function ke Andar = ke Sign se hoty hen
# Lets Suppose

# def add(a, b=b) # Agar Paramter nhi denge to wo automatic b ki argument 3 utha lega
#     return a + b

# sum = add(10, 20)
# print(sum)


# (Methods) is Built in function ...
#1. String Method
#2. List Method
#3. Tuple Method
#4. Dictionary Method

# What is Method? = This is Class Function (Method New Value ko return Karta hy
# what is object?  = koi bhi aisi cheez jo kisi class se Jurri

#1. String Method

# name = "pakistan" # iska first letter small case me hy isko hum Capital Karenge

# print(type(name)) # This is String Type

#  # Ctr + i = open function list

# print(name.capitalize()) # isne first letter ko Capital Kiya ab result ke liye neeche print likhengy
# print(name)

# What is Method?
# Ans. 

# These are Methods Which are Given Below.
#1. String Method
#2. List Method
#3. Tuple Method
#4. Dictionary Method

# These are Six "String Methods" which are Given Below
#1. Count Method 
#2. Length Method
#3. Find Method
#4. Index Method 
#5. Replace Method
#6. Upper Method

abc = "My Name is Jabbar and My Nationality is Pakistani"

print(abc.count('My')) # Count se murad hum word / letter cound karenge
print(len(abc)) # Len se Hum Word ya sentence ki Length Maloom Karenge
print(abc.find('My')) # Find se koi bhi word ya sentence search kar sakte hen
print(abc.index('My')) # Index se Hum Sentence ka Index Maloom Kar sakty hen
print(abc.replace("Jabbar"," Khan").upper()) # Replace karne ke liye Pehle Old Value likhenge phr New likhenge (Change Karenge) or last me Upper Case bhi Kar denge



# These are Six List Methods which are Given Below
#1. Append Method 
#2. Insert Method  
#3. Reverse Method
#4. Pop Method
#5. Remove Method
#6. Sort Method
#7. Extend Method
#8. 



my_list = ["Jabbar","Oshaq","Waqar","Sameen","Kareem"]

# Append = is se last me eik add hoga (List ke End me Add hoga)
my_list.append('Jimmy')
print(my_list)

# Insert: Ye List Ke First me add karega ( Or ye index ke hisab se add karega to Index zarur Lagayenge)
my_list.insert(1, 'Jimmy')
print(my_list)

# Reverse = ye last se leky first tak reverse karega
my_list.reverse(1, 'Jimmy') 
print(my_list)

# Pop : = Jo last wala Hoga wo remove karega (is me hum index dety hen)
my_list.pop()
print(my_list)

# Sort : is se Name wise sort out Karega or iske andar 
my_list.sort(reverse=True)
print(my_list)

# Remove : Ye sirf Specific Value Remove Karega
my_list.remove('Sameen')
print(my_list)


# Extend : Poori List Ko Extend karenge (Merge Karenge) or isko last me 
new_student = ['Kareem','Sameen']
print("Old Student", my_list)
my_list.extend(new_student)
print("Updated List", my_list)


# Dictionay Methods (This Data Type)
# These are Dictionary Methods
#1. Get Method
#2. Keys
#3   Item
#4. Update
#5. Clear()
#6. Pop

# Dictionary pe Hum jab bhi kaam karenge to uski Key Pe Kaam karenge


my_dict = {
    "name" : "Jabbar",
    "Age" : 30,
    "City" : "Karachi",
}


# Keys : ye list format me aayenge saari Keys hamare list ki surat me aayengi (Name, Age, City)
my_dict.keys())

# values : Ye wala Keys ki Value ko list ke format me result dega (List me )
print(my_dict.values())

# Items : Kitne items hen Jo Names Age City hen wo saare items result (Ye list me tuple me result dega, one by one)
print(my_dict.items())

# Others option called --> (Destructuring)
for key, value in my_dict.items():
    print(f"key {key} and value {value}")

 # Get : Eik Nmae key uski Value bata do ()
print(my_dict.get("name"))

 # Update : Ye Dictionary me Jo List hy Usko Update karega
new_dict = {"City" : "Karachi"}
new_dict2 = {"Country" : "Pakistan"}
my_dict.update(new_dict) # Ye 
my_dict.update(new_dict2)
print(my_dict)

# Pop


# Clear : saare items remove kar dega
my_dict.clear()
print(my_dict)


# Tuples ke Methods = Ghar pe parhne hen
#1. Index
#2. Count







