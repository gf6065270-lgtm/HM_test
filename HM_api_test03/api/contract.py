import requests
from HM_api_test03.scripts.config import BASE_URL
class Contract:
    def contract_file(self, token,files):
        return requests.post(BASE_URL + '/api/common/upload',
                             headers={'Authorization': token},
                            files={'file':files})
    def contract_add(self, token, json):
        return requests.post(BASE_URL + '/api/contract',
                            headers={'Authorization': token},
                             json= json)

    def contract_info(self, token, params):
        return requests.get(BASE_URL + '/api/contract/list',
                             headers={'Authorization': token},
                             params=params
                             )
    def contract_delete(self, token, data):
        return requests.post(BASE_URL + '/api/contract/remove',
                             headers={'Authorization': token},
                              data=data
                             )

