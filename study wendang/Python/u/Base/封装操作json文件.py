import json


class OperateJson():
    def __init__(self, file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = r'..\interfaceCase\login.json'
        self.data = self.read_data()

    def read_data(self):
        with open(self.file_path, encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    def get_value(self, id):
        values = self.data[id]
        return values


# if __name__ == '__main__':
#     run = OperateJson()
#     print(run.get_value('loginout'))
