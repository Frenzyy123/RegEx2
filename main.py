import re
user_name = "Jovan123"
print(re.match(r"^[a-zA-Z]{1,5}\d{2,}$",user_name))