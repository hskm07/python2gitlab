# reference : https://docs.gitlab.com/ee/api/api_resources.html

import requests
import json
import pprint

from setting import private_token

from api import get_project



url = "https://gitlab.com/api/v4/projects"

token = {"PRIVATE-TOKEN":private_token}
params = {"visibility":"private"}

# get project for api
get_project(url, headers=token, params=params)


# get issue
url = 'https://gitlab.com/api/v4/issues'
issue_res = requests.get(url, headers=token)
print(issue_res.headers)
issue_json = issue_res.json()
pprint.pprint(issue_json)