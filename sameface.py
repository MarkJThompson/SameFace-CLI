import requests
import json
import sys

apiKey = "**YOUR_KEY_HERE**"

# Documentation for AnalyzeAdult Endpoint
# https://www.haystack.ai/docs?python#analyzeadult
def facesAreSame(imageData1, imageData2):
	outputType = "json"
	requestUri = "https://api.haystack.ai/api/image/verify?output={}&apikey={}".format(outputType, apiKey)
	apiResponse = requests.post(requestUri, files = { 
		"image1": imageData1,
		"image2": imageData2
	})
	response = json.loads(apiResponse.text)

	return response["isSame"]

image1 = sys.argv[1]
image2 = sys.argv[2]

with open(image1, "rb") as imageData1, open(image2, "rb") as imageData2:
	print(facesAreSame(imageData1, imageData2))