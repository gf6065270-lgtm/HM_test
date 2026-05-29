import requests

res2= requests.post(url ='http://121.43.169.97/member/public/sendSms',
         data={
                    "phone":"18332005002",
                    "imgVerifyCode":"8888",
                    "type":"reg"
                })
res3= requests.post(url ='http://121.43.169.97/member/public/reg',
         data={
                    "phone":"18332005002",
                    "password":"123456asd",
                    "verifyCode":"8888",
                   " phone_code":"666666",
                    "dy_server":"on"
                })