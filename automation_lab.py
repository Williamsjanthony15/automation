from locale import locale_encoding_alias
from typing import Text
from faker import Faker
import re


re_phone = re.compile(r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?")

re_email = re.compile(r"\w+.\w+@\w+.\w+.(com|net|org|info|biz)")



all_numbers = []
all_emails = []
filtered_emails = []


period = '.'
dash = '-'
internationl = '+1-'
US = '1'
open_para = '('
closed_para = ')'
seattle = '206-'

   
# read and filter out numbers from our note.txt file
with open('assets/potential_contacts.txt', 'r+') as f:
    content = f.readlines()
    for line in content:
        if re_phone.search(line):
            number = re_phone.search(line)
            number = number.group()
            
            
            if period in number:
                number = number.replace(period, dash)
            if internationl or US in number:
                number = number.strip(internationl)
                number = number.strip(US)
            if open_para in number:
                number = number.strip(open_para)
            if closed_para in number:
                number = number.replace(closed_para, dash)
            
            if len(number) == 10:
                number = number[:3] + dash + number[3:6] + dash + number[6:]
            if len(number) == 7:
                number = number[:3] + dash + number [3:6]
            # if len(number) > 10:
            #      number = seattle + number[:3] + dash + number[4:]
            # if len(number) == 7:
            #     number = seattle + number
            if len(number.split('x')[0]) < 10:
                number = seattle + number
            
            all_numbers.append(number)
            all_numbers = sorted(all_numbers)
            # all_numbers.sorted()   
    
    
    for line in content:
        if re_email.search(line):
            found_email = re_email.search(line)
            found_email = found_email.group()
            emails = sorted(found_email)
            all_emails.append(found_email)
            

# write filtered out numbers to our phone_numbers.txt 
with open('assets/phone_numbers.txt', 'w+') as f:
    for numbers in all_numbers:
        f.write(f'{numbers}\n')
        
                
#write filterd emails to our emails.txt file
with open('assets/emails.txt', 'w+') as f:
    content = f.readlines()
    for email in all_emails:
        f.write(f'{email}\n')