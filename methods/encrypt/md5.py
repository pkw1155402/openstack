#!/usr/bin/env python



import hashlib

def signup(username,pwd):
    '''
    注意：当用户输入注册账号时，应通过js或ajax去判断账号是否存在，而js去判断必须注意进行条件检查，避免sql注入
   将用户账户和密码保存在数据库中，可根据情况增加用户账户的其他属性，比如创建日期、启用/禁用等  
    '''
    
#下面的1可以使用随机变量值代替，但必须将对应的随机变量值也保存起来，以便后续验证使用。
a="123"
encrypwd = hashlib.md5(a+"1")
sign = encrypwd.hexdigest()
print sign