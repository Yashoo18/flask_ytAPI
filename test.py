import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 78, "name":"bro", "views": 1000},
# 		{"likes": 781, "name":"bro1", "views": 31000},
# 		{"likes": 782, "name":"bro2", "views": 21000}]

# for i in range(len(data)):
# 	response = requests.put(BASE + "video/"+ str(i), data[i])
# 	print(response.json())

# input()

# response = requests.delete(BASE + "video/0")
# print(response)
# input()
# response = requests.get(BASE + "video/2")
# print(response.json())

response = requests.patch(BASE + "video/2", {"likes":69})
print(response.json())