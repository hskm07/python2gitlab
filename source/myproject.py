# reference : https://docs.gitlab.com/ee/api/api_resources.html

import requests
import json
import pprint

from setting import private_token

from api import get_project



url = "https://gitlab.com/api/v4/projects"

# token = {"PRIVATE-TOKEN":private_token}
token = {}
params = {"visibility":"private"}
params = {}

# get project for api
ret = get_project(url, headers=token, params=params)


# # get issue
# url = 'https://gitlab.com/api/v4/issues'
# issue_res = requests.get(url, headers=token)
# print(issue_res.headers)
# issue_json = issue_res.json()
# pprint.pprint(issue_json)

# # get list repository 
# url = 'http:/projects/{0}/repository/commits'.format(str(ret[0]['id']))
# commit_list = requests.get(url, headers=token)