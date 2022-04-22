from flask import Flask
from wsgiref.simple_server import make_server 
 
app=Flask(__name__) 
 
@app.route('/')      #路由系统生成 视图对应url,1. decorator=app.route() 2. decorator(first_flask)
def first_flask():    #视图函数
    return 'Hello Worldcaicai'  #response
 
if __name__ == '__main__':
    server = make_server('0.0.0.0', 5000, app)
    server.serve_forever()#启动socket

