#!/usr/bin/python
# by BlackXploits

import smtplib
import getpass

w = '\033[0m'
g = '\033[32m'

# From adrress & To address
fromaddress = raw_input("From address: ")
toaddress = raw_input("To address: ")

# Gmail Login
username = raw_input("Your email: ")
password = getpass.getpass("Password: ")

# Write message
message = raw_input("Your message: ")

# Creating a connection
server =smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

# Creating a for loop to send multiple mails
for i in range (0,10):
  server.sendmail(fromaddress,toaddress,message)
  print g+"[*]"+w+" mail sent !"
  
server.quit()
