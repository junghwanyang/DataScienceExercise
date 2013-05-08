import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=Obama")
pyresponse = json.load(response)

#print type(pyresponse) # dictionary
#print pyresponse.keys()

#print pyresponse["results"]
#print type(pyresponse["results"]) # list

results = pyresponse["results"]

#print the first instance of "results"
#print results[0]

#print type(results[0]) # dict
#print results[0].keys()

# see text of a tweet
#print results[0]["text"]
#print results[3]["text"]

