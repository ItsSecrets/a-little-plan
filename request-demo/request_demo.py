# -*-coding:utf-8 -*-
import requests




URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'


def use_simple_requests():
    response = requests.get(URL_IP)
    print('===========request header=============')
    print response.headers
    print('===========request header=============')

    print('===========request body===============')
    print(response.text)
    # print(response.json())
    print('===========request body===============')

def use_params_requests():
    # 构建参数
    params = {'param1':'hello', 'param2':'world'}

    # 发送请求
    response = requests.get(URL_GET, params)
    # 相应处理
    # 一些常用的api

    # 状态码
    print response.status_code

    # reason
    print  response.reason

    #headers
    print response.headers

    #url
    print response.url

    #encoding
    print response.encoding

    #contnet字符串格式
    print response.content

    #text 转换成编码格式
    print response.text

    # json 转换成一个字典
    print response.json()


    #查看response的内容
    print dir(response)

if __name__ == '__main__':
    print('========simple requests demo:')
    use_simple_requests()

    print('========params requests demo:')
    use_params_requests()