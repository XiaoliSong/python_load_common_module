# 引入backend或者cms的const.app，注意不要用import cosnt.app
from const import app

redis_port = 6379
redis_host = '127.0.0.1'

print(app.app_name + ': redis')