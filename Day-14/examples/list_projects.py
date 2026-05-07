# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://uppalanchi.atlassian.net/rest/api/3/project"

API_TOKEN="ATCTT3xFfGN0EW3DOHV6X0SlQuL52skL1PpZ1m8YT0Z58-bTAfiX4Slm21GsseQOnjlnKKqsP5JgOpoLXHS--IJfDZNLdM1PKDDu0K2DePXjj0R5cxZFWP6HkcHV1s_R3ryr-dibBaxhXzFd_NozkkSeBuj3U11BjbVGJJlp2H7NtBESqk86yaI=F96AF31D"

auth = HTTPBasicAuth("", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)