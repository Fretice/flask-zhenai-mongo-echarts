from . import mongo

class Person_Meizi(mongo.Document):
    edu = mongo.StringField()
    pic_logo = mongo.StringField()
    height = mongo.StringField()
    NickName = mongo.StringField()
    work_location = mongo.StringField()
    zodiac = mongo.StringField()
    vocation = mongo.StringField()
    marry_status = mongo.StringField()
    salary = mongo.StringField()
    MemberId = mongo.StringField()
    age = mongo.StringField()
    hometown_location = mongo.StringField()

    meta = {'collection': 'zhenaidatabase'}
