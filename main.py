import sftp_test
import zip
import ran_name
import json_settings

js = json_settings.settings("settings.json")

con = sftp_test.SFTP(js.pars_json()["login"]["login"],
                     js.pars_json()["login"]["password"],
                     js.pars_json()["remote_serv"]["host"],
                     js.pars_json()["remote_serv"]["port"],
                     js.pars_json()["path"]["local_path"],
                     js.pars_json()["path"]["remote_path"])
con.get_all()
print("Файлы скачаны")

zip = zip.zip_create(ran_name.generate_random_string(30), r"./one/world", r'./backup')
zip.create()
zip.trans_zip()
print("Backup создан успешно")





