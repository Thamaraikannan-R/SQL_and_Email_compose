import re
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
connection = pymysql.connect("46.4.115.158","beo", "beo@123","testdb")
tablename = "signup_reset"
t = 0
while t == 0:
    username = str(input("Enter your user ID: "))
    password = str(input("Enter your password: "))
    action = connection.cursor()
    sql = "select password from " + tablename + " where user_id= '"+username+"'"
    action.execute(sql)
    temp = str(action.fetchall())
    check = str(re.sub('[^\w@#$%]',"",temp))
    title = []
    if password == check:
        print("user name and password verified..!")
        t+=1
    else:
        print("username and password is incorrect try again")
        continue
sql = """desc """+ tablename
action.execute(sql)
temp = action.fetchall()
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
<h2><center>!..Your account details..!</center></h2>
<table style="width:30%">
   <tr	bgcolor="green">"""
for i in temp:
    title.append(str(i[0]))
    if 'password' == (str(i[0])):
        continue
    else:
        html=html+"<th>"+str(i[0])+"</th>"
html = html+"</tr><tr>"
sql = """select *from """ + tablename + " where user_id= '"+username+"'"
action.execute(sql)
temp = action.fetchall()
value = list(temp[0])
sql = """select email_id from """+tablename+" where user_id= '" + username + "'"
action.execute(sql)
temp = str(action.fetchall())
email = str(re.sub('[^\w@._]', "", temp))
connection.commit()
connection.close()
for i in value:
    if i == check:
        continue
    else:
        html = html + "<th>" + i + "</th>"
html = html+"</tr></table></body></html>"
me = "rtkcse2@gmail.com"
you = email
msg = MIMEMultipart('alternative')
msg['Subject'] = "Account Summary..."
msg['From'] = me
msg['To'] = you
part1 = MIMEText(html, 'html')
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('rtkcse2@gmail.com', 'kannankannan')
mail.sendmail(me, you, msg.as_string())
print("Successfully email Sent")

