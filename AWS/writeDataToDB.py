import requests

uri = 'https://l4gv9uqwpd.execute-api.us-west-1.amazonaws.com/prod/sensordata'

requests.put(uri + "?humidity=" + str(hum) + "&temperature=" + str(temp))
