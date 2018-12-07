import pymysql
connection = pymysql.connect("46.4.115.158","beo", "beo@123","testdb")

action = connection.cursor()
table_name=input("Enter table Name:")
sql="""
"""
sql=sql+"create table "+table_name+"("
column=int(input("how many columns:"))
for i in range(1,column+1):
    print("Enter the", i, "Column Name and Data Type(EX: ID INT(20):")
    inp = str(input())
    sql = sql + str(inp)
    if(i<column):
        sql=sql+","
sql=sql+")"
print(sql)
try:
    action.execute(sql)
    connection.commit()
    print('Table created successfully !!!')
except:
    print("Table creation failed !!!")
connection.close()