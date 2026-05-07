# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://uppalanchi.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATCTT3xFfGN0EW3DOHV6X0SlQuL52skL1PpZ1m8YT0Z58-bTAfiX4Slm21GsseQOnjlnKKqsP5JgOpoLXHS--IJfDZNLdM1PKDDu0K2DePXjj0R5cxZFWP6HkcHV1s_R3ryr-dibBaxhXzFd_NozkkSeBuj3U11BjbVGJJlp2H7NtBESqk86yaI=F96AF31D"

auth = HTTPBasicAuth("uppalanchi@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "MyJiraProject"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))