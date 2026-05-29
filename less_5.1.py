import requests
from config import BASE_URL
from tools import login

course_id = "588862"
url = BASE_URL + f'/api/clues/course/{course_id}'  # URL: /api/clues/course/588862

heard = {"Authorization":login()}
res = requests.get(url =url,headers=heard,params={"id": " 9"})
print(res.json())