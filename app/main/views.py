from datetime import datetime
from flask import render_template, session, redirect, url_for, current_app, abort, flash, request, make_response
from . import main
from .. import db
from .. import config
from ..models import Person_Meizi

@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Person_Meizi.objects.paginate(page=page, per_page=current_app.config["FLASK_IMAGES_PER_PAGE"])
    imgs = pagination.items
    return render_template('index.html', imgs=imgs, pagination=pagination)

@main.route('/map', methods=['GET', 'POST'])
def map():
    meizi_list = list(Person_Meizi.objects.all())
    location_list = []
    map_val = {}
    for meizi in meizi_list:
        if meizi.work_location not in location_list:
            location_list.append(meizi.work_location)
            map_val[meizi.work_location]=1
        else:
            map_val[meizi.work_location]+=1
    return_val = []

    for key in map_val.keys():
        new_map = {}
        new_map['name'] = key.replace("北京","")
        new_map['value'] = map_val[key]
        return_val.append(new_map)
    return render_template('index_map.html', map_val=map_val, return_val=return_val)

@main.route('/data_detail', methods=['GET'])
def data_detail():
    return render_template('index_data_detail.html')

@main.route('/get_data/<data_type>', methods=['POST'])
def get_data(data_type):
    meizi_list = list(Person_Meizi.objects.all().order_by(data_type))
    type_list =  []
    type_val = {}
    if data_type == 'age':
        for meizi in meizi_list:
            if meizi.age not in type_list:
                type_list.append(meizi.age)
                type_val[meizi.age]=1
            else:
                type_val[meizi.age]+=1
    elif data_type =='edu':
        for meizi in meizi_list:
            if meizi.edu not in type_list:
                type_list.append(meizi.edu)
                type_val[meizi.edu]=1
            else:
                type_val[meizi.edu]+=1
    elif data_type =='height':
        for meizi in meizi_list:
            if meizi.height not in type_list:
                type_list.append(meizi.height)
                type_val[meizi.height]=1
            else:
                type_val[meizi.height]+=1
    elif data_type == 'marry_status' :
        for meizi in meizi_list:
            if meizi.marry_status not in type_list:
                type_list.append(meizi.marry_status)
                type_val[meizi.marry_status]=1
            else:
                type_val[meizi.marry_status]+=1

    return_val = []
    if data_type == "height" or data_type == "age":
        for type_item in type_list:
            return_val.append(type_val[type_item])
    else :
        for key in type_val.keys():
            new_map = {}
            new_map['name'] = key
            new_map['value'] = type_val[key]
            return_val.append(new_map)

    if data_type == "height" or data_type == "age":
        return str(type_list)+'^'+str(return_val)
    else :
        return str(list(type_val.keys()))+'^'+ str(return_val)
