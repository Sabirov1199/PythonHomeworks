#1Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days
from  datetime import datetime,timedelta
now=datetime.now()

a=input('Enter your Birthday')
birthday = datetime.strptime(a, "%Y-%m-%d")
diff=now-birthday
age=diff.days/365
print (f"You are {age}years old")
#2 Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
now=datetime.now()
a=input('Enter your Birthday')
birthday = datetime.strptime(a, "%Y-%m-%d")
now_year=datetime.now().year
next_birthday=birthday.replace(year=now_year)
if next_birthday<now:
    next_birthday=next_birthday.replace(year=now_year+1)
daysuntillbday=(next_birthday-now).days
print (f" {daysuntillbday}days untill bday")
##3.Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
now = datetime.strptime(input("Current date & time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")

h = int(input("Hours: "))
m = int(input("Minutes: "))

end = now + timedelta(hours=h, minutes=m)
print("Meeting ends at:", end.strftime("%Y-%m-%d %H:%M"))


##4.Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
from datetime import datetime
dt_str=input("Enter date and time")
From_tz=input("Enter your timezone")
to_tz=input("Enter target timezone")

dt=datetime.strptime(dt_str,"%Y-%m-%d %H:%M" )
dt=dt.replace(tzinfo=zoneinfo(From_tz))

converted=dt.astimezone(ZoneInfo(to_tz))
Print("Converted Time ",converted.strftime(("%Y-%m-%d %H:%M (%Z)")))



##5Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
from datetime import datetime
target=input("Enter your target time")
target_time=datetime.strptime(target,"%Y-%m-%d %H:%M:%S")

while True:
    now=datetime.now()
    diff=target_time-now

    if diff.total_seconds()<=0:
        Print("Time is up")
        break
    print("Time left:",str(diff).split('.')[0],end='\r')
    time.sleep(1)

##6.Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re
email= input("Enter your email adress")
pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pattern,email):
    print("emial is valid")
else:
    print("email is not valid")    

##7.Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
number=input("Enter your phone number")
if len(number)==10 and number.isdigit():
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print("formatted phone number",formatted)
else:
    print("please enter exact 10 digits")   
##8.Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
p=input("Enter your password")
if len(p)>=8  and any(c.isupper() for c in p) and any(c.islower() for c in p) and any(c.isdigit()for c in p):
    print("Strong password")
else:
    print("weak passwor")   

##9.Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

text = "Python is fun. Python is easy. I love Python!"
word = input("Enter word: ")

print("Found:", text.lower().count(word.lower()))

##10.Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
import re
text=input("Enter your text")
pattern = r"\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b"

dates = re.findall(pattern, text)
print("Found date",dates)
