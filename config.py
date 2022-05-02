# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'flaskproject1'
USERNAME = 'cwl'
PASSWORD = '123456'
# DB_URI = "mysql+pymysql=//{}={}@{}={}/{}?charset=utf8".format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOSTNAME,port=PORT, db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "ioetetjeitjjm"


MAIL_SERVER = "smtp.163.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "leonchu3@163.com"
MAIL_PASSWORD = "MOZKJEYLSZGABAKJ"
MAIL_DEFAULT_SENDER = "leonchu3@163.com"
