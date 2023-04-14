import requests
import os

class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def authorization(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path:str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload/'
        name = os.path.basename(path_to_file)
        params = {'path': name, 'overwrite': True}
        resp = requests.get(url, headers = self.authorization(), params=params).json()
        upload_link = resp.get('href')
        response = requests.put(upload_link, data=open(file_path, 'rb'), headers=self.authorization())
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.abspath('2/test.txt')
    token = 'y0_AgAAAABpnBJBAADLWwAAAADgygtmJpbqdAn5Rc2c_2Pt3xxJUXnWQ9M'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

