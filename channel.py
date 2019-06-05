import random,time as t

class msg:
    def __init__(self,user,ctime,info):
        self.user = user
        self.info = info
        self.time = ctime

class chnl:

    def __init__(self,id,creator,name):
        self.id = id
        self.name = name
        self.creator = creator
        self.msg_box = []
        self.len = len(self.msg_box)

    def add_message(self,uname,info):
        self.msg_box.append(msg(uname,info))
        self.len += 1

def create_chnl(uname,name):
    id = str(random.randrange(10**8,999999999))
    print(uname,' create chnl:',id ,name)
    with open('static/chnl.txt','a')as f:
        f.write(id+' '+name+' '+uname+'\n')
    with open('static/chnl_msg_box_'+id+'.txt','w')as f:
        f.write('test_user////'+t.strftime("%Y-%m-%d-%H:%M:%S",t.localtime())+'////this is a test\n')
    return

def load_chnl_msg(chnl_id):
    lis = []
    with open('static/chnl_msg_box_'+str(chnl_id)+'.txt','r')as f:
        raw_str = f.read()
    raw_str = raw_str.split('\n')
    del raw_str[-1]
    for i in raw_str:
        uname,ctime,comment = i.split('////')
        lis.append(msg(uname,ctime,comment))
    return lis

def load_chnl():
    lis = []
    with open('static/chnl.txt','r')as f:
        raw_str = f.read()
    raw_str = raw_str.split('\n')
    del raw_str[-1]
    for i in raw_str:
        id,creator,name = i.split(' ')
        lis.append(chnl(id,name,creator))
    return lis


if __name__ == '__main__':
    create_chnl('c1','ch2')
    create_chnl('c1','ch3')
    create_chnl('c2','ch5')
    r = load_chnl()
    print(r)
