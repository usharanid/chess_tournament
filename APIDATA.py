import json,requests,csv
import pandas as pd

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

Actualusers = ['AdithyaT', 'Padmi5', 'HariKnight', 'aradhana15', 'TarikaNaren', 'Divya0311','Anvith2015','Aarav201']


Dict = {}
print("Initial nested dictionary:-")
print(Dict)

Dict['Gnanada(W)'] = {}

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

for i in range(10):
    print(k)
    if data['games'][k]['black']['username'] in Actualusers:

       D = {}
       D['Opponentname'] = data['games'][k]['black']['username']
       D['BlackStatus'] = data['games'][k]['black']['result']
       D['Opponentcolor'] = 'Black'
       Dict['Gnanada(W)']['Opponentname'] = data['games'][k]['black']['username']
       Dict['Gnanada(W)']['WhiteStatus'] =data['games'][k]['white']['result']
       Dict['Gnanada(W)']['Date'] = '2020.04.03'
       Dict['Gnanada(W)']['Opponentcolor'] = 'Black'
       Newlist.append(D)

    if data['games'][k]['white']['username'] in Actualusers:
        D = {}
        D['Opponentname'] = data['games'][k]['white']['username']
        D['WhiteStatus'] = data['games'][k]['white']['result']
        D['Opponentcolor'] = 'White'
        Newlist.append(D)

    k=k+1
    if k == j:
      break

print(Dict)
print(D)
print(Newlist)
print(len(Newlist))

Finaldict={}

Finaldict['gnanada']=Newlist

print(Finaldict)


brics = pd.DataFrame(Finaldict)
print(brics)

with open('mycsvfile1.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, Finaldict.keys())
    w.writeheader()
    w.writerow(Finaldict)


with open('result.json', 'w') as fp:
        json.dump(Finaldict, fp)

read_file = pd.read_csv (r'C:\Users\Ravi\PycharmProjects\Usha\venv\mycsvfile1.csv')
print(read_file)
read_file.to_excel (r'C:\Users\Ravi\PycharmProjects\Usha\venv\Chessgame1.xlsx', index = None, header=True)



