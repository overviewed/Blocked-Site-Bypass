
from webbot import Browser
from time import sleep

web = Browser()
print('================================')
print('Made By: YeetsaJr')
print('g = www.google.com')
print('Use Your own URL')
print('Leave Blank For Default Website')
print('================================')
website = input('Website: ')

if website == 'g':
    web.go_to('https://www.google.com/')

if website == '':
    web.go_to('https://pypi.org/project/webbot')

else:
    web.go_to(website)

while True:
    sleep(0.1)
