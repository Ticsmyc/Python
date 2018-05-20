# -*- coding: utf-8 -*-

import requests

#执行API调用存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code :",r.status_code)

#存储API响应
response_dict=r.json()
print("Total repositories: ",response_dict['total_count'] )

#和仓库有关的信息
repo_dicts=response_dict['items']
print("Repositories returned:", len(repo_dicts))



#输出结果
print(response_dict.keys())