import zipfile, os, glob, shutil

## Создание zip файла и перемещение в нужный каталог
class zip_create():
    ## Часть с инициализацией
    def __init__(self, name, path, path_des):
        self.__name = name
        self.__path = path
        self.__path_des = path_des
        self.__file_dir = glob.glob(self.__path+'**', recursive=True)
    ##Упаковка
    def create(self):
        with zipfile.ZipFile(self.__name+".zip", mode='w',
                             compression=zipfile.ZIP_DEFLATED) as self.__zf:
            for file in self.__file_dir:
                self.__zf.write(file)
        for del_file in self.__file_dir:
            os.remove(del_file)
    ##Перемещение zip файла
    def trans_zip(self):
        shutil.move(self.__name+".zip", self.__path_des)