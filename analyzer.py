import re

with open('logs/http.log','r') as http_file:
    lines = http_file.readlines()

with open('logs/success.log','w') as success_file, open('logs/errors.log','w') as error_file:
    for line in lines:
        if re.search(r"Error \d{3}",line):
            error_file.write(line)
        else:
            success_file.write(line)

