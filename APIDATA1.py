import json,requests,csv
import pandas as pd
import openpyxl
import mysql.connector
import sqlalchemy
import pymysql

# // getting json string.response is json string
response = requests.get("https://api.chess.com/pub/player/gnanada13/games/2020/04")

# // parsing json string.This returns a dictionary.data is json dictionary
data = json.loads(response.text)

#  printing json in pretty format
prettydata = json.dumps(data, indent = 4, sort_keys=True)
with open('C:/Users/Ravi/Desktop/Chess/test.txt', 'w') as outfile:
    outfile.write(str(data))
with open('C:/Users/Ravi/Desktop/Chess/pretty.txt', 'w') as outfile1:
        outfile1.write(prettydata)
print(data)

# for displaying all the data
for k, v in data.items():
    print(k, v)
    print("Hi")

j=len(data['games'])
k=0
# usernames=[]
# usernames1=[]
#
# # TO find out Gnanada has played with which all users
# for i in range(9):
#     print(data['games'][k]['white']['username'])
#     user=data['games'][k]['white']['username']
#     user1=data['games'][k]['black']['username']
#     print(user)
#     usernames.append(user)
#     usernames1.append(user1)
#     k=k+1
#     if k == j:
#       break
# print(usernames)
# print(usernames1)
#
# UsersList = usernames + usernames1
#
# print(UsersList)
# #Removing duplicates from the userslist
# UsersList= list(dict.fromkeys(UsersList))
#
# print(UsersList)

print(len(data['games']))

Actualusers = ['AdithyaT', 'Padmi5', 'gnanada13','HariKnight', 'aradhana15', 'TarikaNaren', 'Divya0311','Anvith2015','Aarav201']




# # Adding elements one at a time
# Dict['Gnanada(W)']['Opponentname'] = 'Bob'
# Dict['Gnanada(W)']['Status'] ="Won"
# Dict['Gnanada(W)']['Date'] = '2020.04.03'
# Dict['Gnanada(W)']['Opponentcolor'] = 'B'
# print("\nAfter adding dictionary Dict1")
# print(Dict)

j=len(data['games'])
k=0
print(data['games'])

Newlist=[]

D={}
for i in range(12):
    if data['games'][k]['black']['username'] or data['games'][k]['white']['username'] in Actualusers:
       print(data['games'][k]['black']['username'])

       D['Game'+str(i)] = {}
       D['Game' + str(i)]['URL'] = data['games'][k]['url']
       D['Game'+str(i)]['Blackusername'] = data['games'][k]['black']['username']
       D['Game' + str(i)]['BlackStatus'] = data['games'][k]['black']['result']
       D['Game' + str(i)]['Whiteusername'] = data['games'][k]['white']['username']
       D['Game' + str(i)]['WhiteStatus'] = data['games'][k]['white']['result']
       k = k + 1
       if k == j:
             break


print(D)
df = pd.DataFrame(D).T
# writer = pd.ExcelWriter('output.xlsx')
# # write dataframe to excel
# df.to_excel(writer)
# # save the excel
# writer.save()

with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, D.keys())
    w.writeheader()
    w.writerow(D)
#
# read_file = pd.read_csv (r'C:\Users\Ravi\PycharmProjects\Usha\venv\mycsvfile.csv')
# print(read_file)
# read_file.to_excel (r'C:\Users\Ravi\PycharmProjects\Usha\venv\Chessgames1.xlsx', index = None, header=True)
#


#        D['Opponentname'] = data['games'][k]['black']['username']
#        D['BlackStatus'] = data['games'][k]['black']['result']
#        D['Opponentcolor'] = 'Black'
#        Dict['Gnanada(W)']['Opponentname'] = data['games'][k]['black']['username']
#        Dict['Gnanada(W)']['WhiteStatus'] =data['games'][k]['white']['result']
#        Dict['Gnanada(W)']['Date'] = '2020.04.03'
#        Dict['Gnanada(W)']['Opponentcolor'] = 'Black'
#        Newlist.append(D)
#
#     if data['games'][k]['white']['username'] in Actualusers:
#         D = {}
#         D['Opponentname'] = data['games'][k]['white']['username']
#         D['WhiteStatus'] = data['games'][k]['white']['result']
#         D['Opponentcolor'] = 'White'
#         Newlist.append(D)
#
#     k=k+1
#     if k == j:
#       break
#
# print(Dict)
# print(D)
# print(Newlist)
# print(len(Newlist))
#
# Finaldict={}
#
# Finaldict['gnanada']=Newlist
#
# print(Finaldict)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Usharani@31",
  database="mydatabase"
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE Chessgames (URL VARCHAR(255), Blackusername VARCHAR(255),BlackStatus VARCHAR(255),Whiteusername VARCHAR(255),Whitestatus VARCHAR(255))")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

for(row,rs) in df.iterrows():
    URL=rs[0]
    Blackusername=rs[1]
    BlackStatus=rs[2]
    Whiteusername=rs[3]
    Whitestatus=rs[4]
    val = (URL,Blackusername,BlackStatus,Whiteusername,Whitestatus)
    query="insert into Chessgames (URL,Blackusername,BlackStatus,Whiteusername,Whitestatus) values (%s,%s,%s,%s,%s)"

    mycursor.execute(query,val)
    mydb.commit()
   # mycursor.close()

mycursor.execute("SELECT * FROM Chessgames")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)