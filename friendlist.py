import facebook
import requests


allfriends = []

graph = facebook.GraphAPI("<Access Token>")
friends = graph.get_connections("me","friends")
allfriends = []

while(True):
    try:
        for friend in friends['data']:
            allfriends.append(friend['name'].encode('utf-8'))

        # Attempt to make a request to the next page of data, if it exists.
        print friends['paging']['next']
        friends=requests.get(friends['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.

        break
i = 0
for a in allfriends:
  print i, a
  i+=1
