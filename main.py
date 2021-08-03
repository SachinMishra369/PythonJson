import json
# data='''
# {
#   "name" : "Chuck",
#   "phone" : {
#     "type" : "intl",
#     "number" : "+1 734 303 4456"
#    },
#    "email" : {
#      "hide" : "yes"
#    }
# }
# '''
# jsondata=json.loads(data)
# print('name is',jsondata['name'])
# print('email is hidden:',jsondata['email']['hide'])
# print('Phone Type:',jsondata['phone']['type'])

# print('Phone Number:',jsondata['phone']['number'])

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''
#loading json data it will remove next line symbol and load it into a proper format
jsonData=json.loads(data)
# print(jsonData)
for item in jsonData:
  print('Id:',item['id'])
  print('X:',item['x'])
  print('Name:',item['name'])


