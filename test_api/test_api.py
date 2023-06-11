import requests

HOST = 'http://127.0.0.1:8000'
res = requests.post(HOST + '/api-token-auth/', {
    'username': 'username',
    'password': 'password',
})

res.raise_for_status()
token = res.json()['token']
print(token)

headers = {'Authorization': 'JWT' + token, 'Accept': 'application/json'}

data = {
    'title': '제목 by code',
    'text': 'API내용 by code',
    'created_date': '2023-06-01T18:00:00+09:00',
    'published_date': '2023-06-01T18:00:00+09:00'
}
file = {'image': open('/Users/jimin/Desktop/test03.jpg', 'rb')}
res = requests.post(HOST + '/api_root/Post/', data=data,
                    files=file, headers=headers)
print(res)
print(res.json())
