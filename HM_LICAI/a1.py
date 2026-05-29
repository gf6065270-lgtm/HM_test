
import requests
seen = requests.session()
res = requests.get("http://121.43.169.97/common/public/verifycode1/0.088340864368183")
# print(res.content)
# print(res.status_code)
with   open("code.png","wb")as f:
    f.write(res.content)

res2= seen.post(url ='http://121.43.169.97/member/public/sendSms',
         data={
                    "phone":"18332005005",
                    "imgVerifyCode":"8888",
                    "type":"reg"
                },cookies=res.cookies)
print(res2.json())
# res3= seen.post(url ='http://121.43.169.97/member/public/reg',
#          data={
#                     "phone":"18332005002",
#                     "password":"123456asd",
#                     "verifyCode":"8888",
#                    "phone_code":"666666",
#                     "dy_server":"on"
#                 },cookies=res.cookies)
# print(res3.json())