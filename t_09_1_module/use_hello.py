# import 模块 vs from 模块 import 模块中的函数

## import 模块
### import 模块 => import 一个文件夹

## from 模块 import 模块中的函数
### from 模块 import 模块中的函数 => from 文件夹 import 文件夹中的一个文件
##-> 实例
### from 什么呢，from 一个目录，名称是t_09_0_module
### import 什么呢，模块中的一个文件，名称是hello.py

from t_09_0_module import hello

def hello_world():
    hello.test1()


hello_world()