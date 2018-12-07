import pymysql
import re
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
username = str(np.random.randint(1111, 9999))
name = input("Enter your Name: ")
username="LT"+username
t = 0
while (t == 0):
    email = input("Enter your Email ID: ")
    if (re.search("[\w,.$]{5,40}@[\w,.]{3,20}", email)):
        email = email
        t = t + 1
    else:
        print("Wrong Email ID retry again")
        continue
password=str(np.random.randint(100000,999999))
sql = """insert into signup_reset values("""
sql = sql + "'" + username + "','" + name + "','" + email + "','" + password + "')"
print(sql)
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
html = html = html + "<tr><th>" + username + "</th><th>" + password + "</th></tr></table></body></html>"""
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
