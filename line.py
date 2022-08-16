# coding: UTF-8
import requests

access_token="取得したトークンをコピペしてください。"
url="https://notify-api.line.me/api/notify"

message="test"

headers = {'Authorization': 'Bearer ' + access_token}
payload = {'message': message}

requests.post(url,headers=headers,data=payload)