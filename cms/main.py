# load_common需要在引入公共模块前引入、最好放在最前面
from util import load_common
from const import app

# 加载公共模块
# 注意不能用import const.redis
from const import redis
# 注意不能用import const.db
from const import db

if __name__=='__main__':
    print(redis.redis_port)
    print(db.db_port)
    print(app.app_name)