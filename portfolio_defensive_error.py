while True:
    user_name = input("Please enter your first name:").lower()
    if user_name.isalpha():
        break
    else:
        print("Please enter valid name.")

while True:
    user_surname = input("Please enter your surname:").lower()
    if user_surname.isalpha():
        break
    else:
        print("Please enter valid surname.")

while True:
    try:
        user_age = int(input("Please enter your age:"))
        break
    except ValueError:
        print("please enter valid number.")

while True:

    user_mobile_number = \
        input("Please enter your mobile number without leading 0:")
    if len(user_mobile_number) == 10 and user_mobile_number.isdigit():
        break
    else:
        print("Please enter 10 digit mobile number only without leading 0")

while True:
    user_email_id = input("Please enter your email id:")
    if "@" in user_email_id and "." in user_email_id:
        break
    else:
        print("Please enter valid email address")

user_address = input("Please enter your full address:")

while True:

    user_skills = input("Please enter your 3 skills following by coma:")
    list_skills = user_skills.strip().split(",")

    if len(list_skills) == 3:
        break
    else:
        print("Please enter your 3 skills.")

while True:

    user_programming_language = \
        input("Please enter upto 3 programming" +
              "languages you know following by coma:")
    list_programming_language = user_programming_language.strip().split(",")
    if len(list_programming_language) <= 3:
        break
    else:
        print("Please enter valid input")

start = "\033[1m"
end = "\033[0;0m"
blue = "\033[0;34m"
bright_yellow = "\033[0;93m"
green = "\033[0;32m"
white = "\033[0;37m"
print()
print(f"{bright_yellow}{start}Here is your complete information:{end}")
print()
print(f"{bright_yellow}{start}Full name{end}:", green + user_name + " "
      + user_surname)
print(f"{bright_yellow}{start}Age{end}:", green + user_age)
print(f"{bright_yellow}{start}Mobile number{end}:", green + user_mobile_number)
print(f"{bright_yellow}{start}Email address{end}:", green + user_email_id)
print(f"{bright_yellow}{start}House address{end}:", green + user_address)
print(f"{bright_yellow}{start}Skills{end}:", green + user_skills)
print(f"{bright_yellow}{start}Programming language{end}:",
      green + user_programming_language)
