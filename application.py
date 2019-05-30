import os

from flask import Flask,render_template,make_response,request
from channel import *
from flask_socketio import SocketIO, emit

app = Flask(__name__)
# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# socketio = SocketIO(app)


@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if not name:
            chnl_name = request.form.get('cname')
            uname = request.cookies.get('uname')
            create_chnl(uname,chnl_name)
            return render_template('index.html', username=name,msg='Channel '+chnl_name+' created!')
        resp = make_response(render_template('index.html', username=name))
        resp.set_cookie('uname', name)
        resp.set_cookie('is_set', '1')
        return resp
    else:
        ck = request.cookies.get('is_set')
        if not ck or ck == '0':
            return render_template('index.html')
        else:
            name = request.cookies.get('uname')
            return render_template('index.html',username=name)

@app.route("/channel")
def channel():
    ck = request.cookies.get('is_set')
    if not ck or ck == '0':
        return render_template('index.html', msg='Cannot enter chnl, please write down your name!')
    else:
        name = request.cookies.get('uname')
        chnl_lis = load_chnl()
        return render_template('channel.html',username=name,lis=chnl_lis)

@app.route("/message")
def message():

    name = request.cookies.get('uname')
    if name:
        return render_template('message.html', username=name)
    else:
        return render_template('message.html')

@app.route("/del_cookie",methods=['POST'])
def del_cookie():
    s = "You have delete the cookie!"
    resp = make_response(s)
    resp.set_cookie('is_set','0')
    resp.delete_cookie('uname')
    resp.delete_cookie('chnl_id')
    return resp


