# Project 2

Web Programming with Python and JavaScript

---

Ver 1：2019-5-30 17:17:43

实现简单cookie，创建channel；（requirments 1-3）

---

Ver 2：2019-6-5 16:10:01

实现channel查看，发送以及查看message；

删除cookie；

---
Ver 3：2019-6-6 11:12:54
实现实时通信，通过socketio实现客户端轮询。

PS：没有实现服务器端主动发送消息给客户端，因为反复测试只有两种情况：
1.只有收到客户端的websocket服务器端才会发送请求，并不是真正意义上的主动发送；
2.客户端每更新留言时若服务器端主动发送websocket，不论广播与否该客户端本身都收不到websocket信息。
详见：[Flask-websocket Emit主动发送消息失败](https://segmentfault.com/q/1010000012605133/a-1020000012616493)

简单示例：
![](https://github.com/marktreyvon/project2-marktreyvon/blob/master/img/eg(1).png)
![](https://github.com/marktreyvon/project2-marktreyvon/blob/master/img/eg(2).png)
![](https://github.com/marktreyvon/project2-marktreyvon/blob/master/img/eg(3).png)
