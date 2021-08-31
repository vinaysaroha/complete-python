import re
# phone number (555)-555-5555
# r"(\d\d\d)-\d\d\d-\d\d\d\d" ----> \d is digit
#       or
# r"(\d{3)-\d{3}-\d{4}"

text = "The agent's phone number is 408-555-1234 . Call Sool !"
print('phone' in text)
import re
pattern = 'phone'
match = re.search(pattern,text) # tell index number of first pattern match
# to find all match
text1 = 'my phone , phone is wringing and I think we have to find phone into the house'
for match in re.finditer('phone',text1):
    print(match)

# \d - digit
# \w - Aphanumeric with _ (underscore)
# \s - white space
# \D - A non digit
# \W - Non-alphanumeric special symbols
# \S - Non-WhiteSpace


phone = re.search('\d{3}-\d{3}-\d{4}',text)
print(phone.group()) # - to group them

# Quantifiers
# + occurs one or more times
# {3} occurs exactly 3 times
# {2,4} occurs 2 to 4 times
# * occurs zero or more time
# ? once or none

phone5 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# if I want its area code that's start 3 digit number than I can get that
result=re.search(phone5,text)
print(result.group(1))
