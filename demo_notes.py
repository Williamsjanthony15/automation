## Automation Lab Demo
# Create Fakes.py

# Import Faker
from faker import Faker 

#Set language for faker
fake = Faker('en_US')

# print(fake)

# This tells me all of the methods i can fake with this object
print(dir(fake))

# Random Names it will generate upon running the script
print(fake.name())

# Random City
print(fake.city())

# Random Credit Card
print(fake.credit_card())

# Giving 100 Names
# If dont want duplicates put names in set
# First name female
for i in range(100):
    print(fake.first_name_female())



# Returns a string of word(s)
print(fake.word())
# Returns a list of 3 words Can have as many words as you want by calling a number.
print(fake.words())
#returns a string of words
print(fake.sentance())
# Returns a list of sentenaces
print(fake.sentenaces())
#Returns a paragraph
print(fake.paragraph())
#return paragraphs
print(fake.paragraphs())
#return email Gives you multiple emails
for i in range(10):
    print(fake.email())
#return phone number
print(fake.phone_number())


# making a file with paragraphs, emails, and phone numbers
content = ''

for i in range(100):
    content += fake.paragraph(2)
    content += fake.email()
    content += fake.paragraph(2)
    content += fake.phone_number()
    content += fake.paragraph()
    # each set of data to be own line
    content += '/n'
print(content)

#Createing a write file with content in it and put it in the assets folder
with open('assets/notes.txt', 'w+') as f:
    f.write(contents)

#Reading the written file with the content in it
with open('assets/notes.txt', 'w+') as f:
    f.read(contents)

#poetry a While reading the file, If it meets the phone numbers description Move it to Phone_Number.txt file
# If it meets the email description move it to the Email.txt file


# copying the created file from assets into demo folder
import shutil

shutil.copy('assets/notes.txt', '.')

#moving created file from assets into demo folder

shutil.move('assets/notes.txt', '.')


