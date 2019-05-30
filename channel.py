import random,time as t

class chnl:

    def __init__(self,id,creator,name):
        self.id = id
        self.name = name
        self.creator = creator
        self.msg_box = [['test','this is test',t.strftime("%Y-%m-%d-%H:%M:%S",t.localtime())]]
        self.len = len(self.msg_box)

    def add_message(self,uname,time,msg):
        self.msg_box.append([uname,msg,time])
        self.len += 1

def create_chnl(uname,name):
    id = str(random.randrange(10**8,999999999))
    print(uname,' create chnl:',id ,name)
    with open('chnl.txt','a')as f:
        f.write(id+' '+name+' '+uname+'\n')
    return chnl(id,uname,name)

def load_chnl():
    lis = []
    with open('chnl.txt','r')as f:
        raw_str = f.read()
    raw_str = raw_str.split('\n')
    del raw_str[-1]
    for i in raw_str:
        id,creator,name = i.split(' ')
        lis.append(chnl(id,creator,name))
    return lis


if __name__ == '__main__':
    create_chnl('c1','ch2')
    create_chnl('c1','ch3')
    create_chnl('c2','ch5')
    r = load_chnl()
    print(r)
