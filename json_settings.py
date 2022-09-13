import json

class settings():
    def __init__(self, json_file):
        self.__json_file = json_file
    def pars_json(self):
        with open(self.__json_file, "r") as self.__read_file:
            self.__data = json.load(self.__read_file)
        return self.__data