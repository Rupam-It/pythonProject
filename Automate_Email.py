#This code is for automate password

import smtplib as s

my_email="example@gmail.com"
password="example" #this password has been deleted , create a new password

connection= s.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="it2021072@rcciit.org.in",msg="this is a python generated mail")
connection.close() 