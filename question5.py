import time

import datetime
Name=raw_input("Enter your Name:")

Age=int(input("Enter your Age:"))

#print '/n'Prac

print 'Hi %s ,Your present Age is %d'%(Name,Age) 
#print '/n'  
#cd=time.strftime("%d/%m/%Y") 
#cd-age 
#print cd.year

cd1=datetime.datetime.now()

cdy=cd1.year
by=int(cdy-Age)

print 'Your Bday year is %d'%by

#print '/n'

by1=int(by+100)

print 'Your age will be 100 years by %d'%by1


