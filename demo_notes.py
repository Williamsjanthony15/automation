## Automation Lab Demo
# Create Fakes.py

# Import Faker
from faker import Faker 
import shutil
import re

#Set language for faker
fake = Faker('en_US')

# print(fake)
# This tells me all of the methods i can fake with this object
# print(dir(fake))
# Random Names it will generate upon running the script
# print(fake.name())
# Random City
# print(fake.city())
# Random Credit Card
# print(fake.credit_card())
# Giving 100 Names
# If dont want duplicates put names in set
# First name female
# for i in range(100):
    # print(fake.first_name_female())
# Returns a string of word(s)
# print(fake.word())
# Returns a list of 3 words Can have as many words as you want by calling a number.
# print(fake.words())
#returns a string of words
# print(fake.sentance())
# Returns a list of sentenaces
# print(fake.sentenaces())
#Returns a paragraph
# print(fake.paragraph())
#return paragraphs
# print(fake.paragraphs())
#return email Gives you multiple emails
# for i in range(10):
    # print(fake.email())
#return phone number
# print(fake.phone_number())
# string = '\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$'
string = '.\d\d\d[.-]\d\d\d[.-]\d\d\d[.-]\d\d\d\d[x,X]\d\d\d\d\d'
# string = '/^\b\d{3}[-.]?\d{3}[-.]?\d{4}\b$/'

# making a file with paragraphs, emails, and phone numbers

content = ''
for i in range(10):
    para = fake.sentence() + ' '
    email = fake.email('gmail.com')
    phone = fake.phone_number()
    content += f'{para} {email} {phone} \n'

#Createing a write file with content in it and put it in the assets folder
with open('assets/paragraph.txt', 'w+') as f:
    f.write(content)


# #Reading the written file with the content in it
with open('assets/paragraph.txt', 'r') as f:
    results = f.read()
    find_number = re.findall(string, content)

print(find_number)
# shutil.copy('assets/phone_numbers.txt', results)

# print(find_number)
#poetry a While reading the file, If it meets the phone numbers description Move it to Phone_Number.txt file
# If it meets the email description move it to the Email.txt file


# copying the created file from assets into demo folder

# shutil.copy('assets/notes.txt', '.')

#moving created file from assets into demo folder

# shutil.move('assets/notes.txt', '.')


