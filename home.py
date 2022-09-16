from flask import Blueprint, render_template

homepg = Blueprint("homepg",__name__)

#home
@homepg.route('/')
def hello_world():
    return render_template('home.html')

#list
@homepg.route('/listblog/')
def list_bloger():
    return render_template('listblog.html')
    
#none
@homepg.route('/listblog/dientu/')
def electrical_ss():
    return render_template('electrical.html')
