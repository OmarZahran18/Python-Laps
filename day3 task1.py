# You are given a list of email addresses in the format username@domain Your task is to use the map()
# function along with a lambda  domain part from each email address
 
emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "mohamed@outlook.com",
    "noha@iti.gov.eg"
]

part_of_emails = map(lambda E: E.split ('@')[1], emails)
print (list(part_of_emails))