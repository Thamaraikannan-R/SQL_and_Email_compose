import pymysql
import re
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

id = str(np.random.randint(11111, 99999))
name = input("Enter your Name: ")
age = str(input("Enter your Age in year: "))
gender = input("Enter your gender(male or female or other):")
t = 0
while (t == 0):
    email = input("Enter your Email ID: ")
    if (re.search("[\w,.$]{5,40}@[\w,.]{3,20}", email)):
        email = email
        t = t + 1
    else:
        print("Wrong Email ID retry again")
        continue
while (t == 1):
    password = str(input("Enter your password: "))
    confirm_password = str(input("Confirm your password:"))
    if (password == confirm_password):
        password = confirm_password
        t = t + 1
    else:
        print("Confirm password incorrect,", end='')
        continue
# this part is sql
sql = """insert into signup values("""
sql = sql + "'" + id + "','" + name + "','" + age + "','" + gender + "','" + email + "','" + password + "')"
# This is part of sqlconnection and innsert new data
connection = pymysql.connect("46.4.115.158", "beo", "beo@123", "testdb")
action = connection.cursor()
action.execute(sql)
connection.commit()
connection.close()
# This is email conformation part
html = """
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td{
    border: 1px solid black;
    border-collapse: collapse;

}
th, td ,tr{
    padding: 10px;
    text-align: centre;

}
</style>
</head>
<body>
<center>
<h2><center>Thank you for register to us...</center></h2>
<table style="width:30%">
   <tr	bgcolor="pink">
    <th>User ID</th>
    <th>Password</th>
   </tr>
  """
html = html = html + "<tr><th>" + id + "</th><th>" + password + "</th></tr></table></body></html>"""
me = "rtkcse2@gmail.com"
you = email
msg = MIMEMultipart('alternative')
msg['Subject'] = "Account has been created!!!"
msg['From'] = me
msg['To'] = you
part1 = MIMEText(html, 'html')
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('rtkcse2@gmail.com', 'kannankannan')
mail.sendmail(me, you, msg.as_string())
print("Sucessfully email Sent")