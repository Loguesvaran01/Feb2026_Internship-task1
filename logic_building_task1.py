# User Login Check
s_uname='admin'
s_pass='1234'

user_n=input("Enter a name:")
user_p=input("Enter a Password:")

if(s_uname==user_n and s_pass==user_p):
    print("Login Successful")
else:
    print("Invalid Credentials")


# Pass / Fail Analyzer
marks=[45, 78, 90, 33, 60]
p_count=0
f_count=0
for m in marks:
    if(m>=50):
        p_count +=1
    else:
        f_count +=1
print("Total Students:", len(marks))
print("Passed Students:", p_count)
print("Failed Students:", f_count)

#Simple Data Cleaner

names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    cleaned_names.append(name.strip().lower())

print(cleaned_names)


# Message Length Analyzer
messages = ["Hi", "Welcome to the platform", "OK"]

for msg in messages:
    print("Message:", msg)
    print("Length:", len(msg))
    
    if len(msg) > 10:
        print("Long message")
    
    print()



#Error Message Detector
logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

for log in logs:
    if log == "ERROR":
        error_count += 1

print("Number of ERROR messages:", error_count)
