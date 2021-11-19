import requests
import json
import textwrap


def get_project(url, headers, params):
    res = requests.get(url, headers=headers, params=params)
    res_json = res.json()
    for r in res_json:
        result=f"""
        id                  : {r['id']}
        description         : {r['description']}
        Project Name        : {r['name']}
        name_with_namespace : {r['name_with_namespace']}
        path_with_namespace : {r['path_with_namespace']}
        created_at          : {r['created_at']}
        branch              : {r['default_branch']}
        ssh_url_to_repo     : {r['ssh_url_to_repo']}
        http_url_to_repo    : {r['http_url_to_repo']}
        """
        print(textwrap.dedent(result))
    return res_json
