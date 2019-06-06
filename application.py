import os

from flask import Flask,render_template,make_response,request
from channel import *
from flask_socketio import SocketIO, emit
import json

app = Flask(__name__)
# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
name_space = '/'
@socketio.on('c',namespace=name_space)
def fresh_msg(data):
    # print(data)
    chnl_id = data['chnl_id']
    print(chnl_id)
    msg_lis = load_chnl_msg_lis(chnl_id)
    msg_lis = json.dumps(msg_lis)
    socketio.sleep(5)
    socketio.emit('server_comment_fresh',msg_lis,json=True)


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
        return render_template('index.html', msg='Cannot enter channel lists, please write down your name!')
    else:
        name = request.cookies.get('uname')
        chnl_lis = load_chnl()
        return render_template('channel.html',username=name,lis=chnl_lis)

@app.route("/message/<int:chnl_id>")
def message(chnl_id):
    ck = request.cookies.get('is_set')
    if not ck or ck == '0':
        return render_template('index.html', msg='Cannot enter chnl, please write down your name!')
    else:
        msg_lis = load_chnl_msg(chnl_id)
        chnl_lis = load_chnl()
        current_chnl = None
        for i in range(len(chnl_lis)):
            if str(chnl_lis[i].id) == str(chnl_id):
                current_chnl = chnl_lis[i]
        name = request.cookies.get('uname')
        if name:
            resp = make_response(render_template('message.html', username=name,current_chnl=current_chnl,msg_lis=msg_lis))
            resp.set_cookie('last_chnl',str(chnl_id))
            return resp
        else:
            return render_template('message.html',current_chnl=current_chnl,msg_lis=msg_lis)

@app.route("/add_comment",methods=['POST'])
def add_comment():
    s = "You have send message successfully!"
    chnl_id = request.referrer[-9:]
    info = request.form.get('info')
    last_chnl = request.cookies.get('last_chnl')
    uname = request.cookies.get('uname')
    ctime = t.strftime("%Y-%m-%d-%H:%M:%S",t.localtime())
    with open('static/chnl_msg_box_'+chnl_id+'.txt','a')as f:
        f.write(uname+'////'+ctime+'////'+info+'\n')
    resp = make_response('<script>alert("'+s+'");location.href="/message/'+last_chnl+'"</script>')

    emit('server_comment_fresh1', {'uname': uname, 'ctime': ctime, 'info': info},namespace=name_space,broadcast=True)
    print(chnl_id,info,uname)

    return resp

@app.route("/del_cookie",methods=['POST'])
def del_cookie():
    s = "You have delete the cookie!"
    resp = make_response('<script>alert("'+s+'");location.href="/"</script>')
    resp.set_cookie('is_set','0')
    resp.delete_cookie('uname')
    resp.delete_cookie('chnl_id')
    return resp

if __name__ == '__main__':
    socketio.run(app)
