import requests

from HM_api_test03.scripts.config import BASE_URL


class Course:
    def add_course(self, token, json_data):
        return requests.post(BASE_URL + '/api/clues/course',
                             headers={'Authorization': token},
                             json=json_data)

    def get_course_list(self, token, params):
        return requests.get(BASE_URL + '/api/clues/course/list',
                            headers={'Authorization': token},
                            params=params)

    def get_course_by_id(self, token, course_id):
        """根据ID获取课程详情"""
        return requests.get(f'{BASE_URL}/api/clues/course/{course_id}',
                            headers={'Authorization': token})

    def update_course(self, token, json_data):
        return requests.put(BASE_URL + '/api/clues/course',
                            headers={'Authorization': token},
                            json=json_data)
    def delete_course(self, token, course_id):
        return requests.delete(f'{BASE_URL}/api/clues/course/{course_id}',
                               headers={'Authorization': token})
