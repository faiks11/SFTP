import pysftp
## Подключение по sftp
class SFTP():
    ## Часть с инициализацией
    def __init__(self, login, password, host, port, local_path, remote_path):

        self.__login = login
        self.__password = password

        self.__host = host
        self.__port = port

        self.__local_path = local_path
        self.__remote_path = remote_path
        self.__listdir = []
        self.__local_filelist = []

        self.__cnopts = pysftp.CnOpts(knownhosts='known_hosts')
        self.__cnopts.hostkeys = None

        self.__sftp = None
        self.__while_var = 0

    ## Получаение всех файлов с сервера
    def get_all(self):
        with pysftp.Connection(host=self.__host, username=self.__login, password=self.__password,cnopts=self.__cnopts, port=self.__port) as self.__sftp:
            print("Подключение установленно")
            self.__listdir = self.__sftp.listdir()
            print(self.__local_path + self.__remote_path)
            self.__sftp.get_r(self.__remote_path, self.__local_path, preserve_mtime=True)