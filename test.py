# counts = dict()
# line = input('enter a line of text: ')
# words = line.split()

# print('Words', words)
# print('Counting...')

# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print('Counts', counts)

# *********

# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
# for k, v in d.items():
#     print(k, v)

# tups = d.items()
# print(tups)

# *********

# d = {'a': 1, 'c': 2, 'b': 3}
# print(d)

# tups = d.items()
# print(tups)

# tups = sorted(d.items())
# print(tups)

# *********

# d = {'a': 1, 'c': 2, 'b': 3}
# tups = d.items()
# for k, v in sorted(d.items()):
#     print(k, v)

# *********

# d = {'a': 2, 'c': 1, 'b': 3}
# tmp = list()
# for k, v in d.items():
#     tmp.append((v, k))
# print(tmp)

# tmp = sorted(tmp, reverse=True)
# print(tmp)

# *********

# fhand = open('text.txt')
# d = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         d[word] = d.get(word, 0) + 1

# l = list()
# for key, val in d.items():
#     tups = (val, key)
#     l.append(tups)

# l = sorted(l, reverse=True)

# for val, key in l[:10]:
#     print(key, val)

# *********

# List Comprehension
# d = {'a': 10, 'b': 1, 'c': 22}
# print(sorted([(v, k) for k, v in d.items()], reverse=True))

# *********

# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)

# *********

# import urllib.request
# import urllib.parse
# import urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# *********

# import urllib.request
# import urllib.parse
# import urllib.error
# from bs4 import BeautifulSoup

# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# *********

# import json

# data = '''
# {
#     "name" : "Chuck",
#     "phone": {
#         "type": "intl",
#         "number": "+1 555 555 5555"
#     },
#     "email": {
#         "hide": "yes"
#     }
# }
# '''

# info = json.loads(data)
# print('Name:', info['name'])
# print('Hide:', info['email']['hide'])

# *********

# import json

# input = '''
# [
#     {
#         "id": "001",
#         "x": "1",
#         "name": "Chuck"
#     },
#     {
#         "id": "002",
#         "x": "2",
#         "name": "Chuck"
#     }
# ]
# '''

# info = json.loads(input)
# print('User Count:', len(info))

# for item in info:
#     print('Name:', item['name'])
#     print('Id:', item['id'])
#     print('Attribute', item['x'])

# *********

# import urllib.request
# import urllib.parse
# import urllib.error
# import json

# service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1:
#         break

#     url = service_url + urllib.parse.urlencode({'address': address})
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')

#     try:
#         js = json.load(data)
#     except:
#         js = None

#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('=== Failure To Retrieve ===')
#         print(data)
#         continue

#     lat = js["results"][0]['geometry']['location']['lat']
#     lng = js["results"][0]['geometry']['location']['lng']
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)

# *********
