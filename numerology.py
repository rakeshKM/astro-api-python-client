import sdk
import json


userID = "624889"
apiKey = "2ce0bc7d506e41013577a8a550b82912"

# dateOfBirth = 17
# monthOfBirth = 10
# yearOfBirth = 1990
# name = 'Rakesh Kumar Mallik'

dateOfBirth = 19
monthOfBirth = 7
yearOfBirth = 1998
name = 'Barnali Sarkar'


# Numerology APIs which needs to be called
resource = 'numero_table'

# instantiate AstrologyAPIClient class
astrologyAPI= sdk.AstrologyAPIClient(userID, apiKey)

# call numerology method of the AstrologyAPIClient
numeroData = astrologyAPI.numeroCall(resource, dateOfBirth, monthOfBirth, yearOfBirth, name)

loaded_json = json.loads(numeroData.text)

print(loaded_json)  # <== prints json response.

# # printing data
# print(numeroData)