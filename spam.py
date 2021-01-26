#!/usr/bin/env python3
# by BlackXploits
# GitHub: https://github.com/blackxploits

import smtplib
import getpass

w = '\033[0m'
g = '\033[32m'
c = '\033[1;36;40m'

# From adrress & To address
fromaddress = input("From address: ")
toaddress = input("To address: ")

# Gmail Login
username = input("Your email: ")
password = getpass.getpass("Password: ")

# message
message = input("Your message: ")

# Creating a connection
server =smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

# for loop to send multiple spam
total = input("Total spam: ")
print (c+"\n[*]"+w+" Running . . ."+w)
for i in range (total):
  server.sendmail(fromaddress,toaddress,message)
  print (g+"[*]"+w+" MAIL SENT !")
  
server.quit()
