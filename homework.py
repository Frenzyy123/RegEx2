import re
from datetime import datetime

def is_date(s):
    match =  re.match(r"\d{4} \d{2} \d{2} \d{2} \d{2} \d{2}", s)
    if match:
        return match.group()
    return None

def get_average():
    with open("logs/errors.log","r") as f:
        lines = f.readlines()
    first_error = is_date(lines[0])
    last_error = is_date(lines[-1])
    if first_error and last_error:
        first_time = datetime.strptime(first_error, "%Y %m %d %H %M %S")
        last_time = datetime.strptime(last_error, "%Y %m %d %H %M %S")
        return (last_time - first_time) // len(lines)
    print("There was an error with importing errors")
    #ovaj print ne bi trebao nikad da se desi
    return None

print(get_average())