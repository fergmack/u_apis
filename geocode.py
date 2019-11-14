# http client library
import httplib2
# for converting in-memory python objects to 
#...a serialised json representation
import json

def getGeocodeLocation(inputString):
	google_api_key = 'AIzaSyA6TMKWZyns8iPDzv7waQ4Z2lyXWmUPpiE'
	locationString = inputString.replace(" ", "+")
	url = ('https://maps.googleapiscom/maps/api/geocode/json?address=%s&key=%s'% 
		(locationString, google_api_key))
	# create instance of http class
	h = httplib2.Http()
	# you can now create a git request with the GET method
	response, content = h.request(url, 'GET')
	# the above request will return an array with two values
	#...the http response, and the content
	# call the below to have it in the correct json format
	result = json.loads(content)
	print "response header: %s \n \n" % response
	return result
