# 引入backend或者cms的const.app，注意不要用import cosnt.app
from const import app

db_port = 3306
db_host = '127.0.0.1'
db_user = 'test'
db_pw = 'test'
db_name = 'test'

print(app.app_name + ': db')