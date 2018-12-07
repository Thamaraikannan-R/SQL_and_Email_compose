import pymysql
import re
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
connection = pymysql.connect("46.4.115.158","beo", "beo@123","testdb")
action = connection.cursor()
username=str(input("Enter your username: "))
t=0
while(t==0):
    password = str(input("Enter your password: "))
    sql = """select password from signup_reset where user_id=""" + "'" + username + "'"
    action.execute(sql)
    temp = str(action.fetchall())
    check = str(re.sub('[^\w@#$%]', "", temp))
    if(password==check):
        new_password=str(input("Enter new password: "))
        new_confirm=str(input("confirm new password:"))
        if(new_password==new_confirm):
            print("New password has been updated")
            t=1
        else:
            print("new password and confirm passowrd incorrect,")
            continue
    else:
        print("Entered password is incorrect")
        continue
sql="""update signup_reset set password = """+"'"+new_password+"'"+" where password = '"+password+"'"
action.execute(sql)
sql = """select email_id from signup_reset where user_id=""" + "'" + username + "'"
action.execute(sql)
temp = str(action.fetchall())
email = str(re.sub('[^\w@._]', "", temp))
print(email)
connection.commit()
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
<h2><center>Password has been changed...</center></h2>
<table style="width:30%">
   <tr	bgcolor="green">
    <th>User ID</th>
    <th>New_Password</th>
   </tr>
  """
html = html = html + "<tr><th>" + username + "</th><th>" + new_password + "</th></tr></table></body></html>"""
me = "rtkcse2@gmail.com"
you = email
msg = MIMEMultipart('alternative')
msg['Subject'] = "Account has been updated!!!"
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

