# Error Handling (Topic)
# means Hum jo code karte hen us me us code ki wajah se hamara 
  
#1. Abnormal Termination -->
#2. Graceful Terminationation --> Error Handling karte (Try except) ye tareeqa hy error Handling karne ka
# is error aayega bhi to Program chalta rahega


num: int = 10
num2: int = 0
result = num / num2
print(result)

try:  # koi bhi kaam karo ... agar ooper koi error aaya to Exception me chala jayega
    print(result)
except Exception as e:     # except Error get karta hy
    pritn(e)

    # Types of Error
    # Key Error
    # Index Error
    # Value Error
    # Import Error

num: int = 10
num2: int = 0
try: 
    result = num / num2
    print(result)
except ZeroDivisionError:
    print("This is Error for zero Value")
except IndexError:
    print("this is Error with Index")

#  

user input se Table Banana hy phr us se try except use karna hy