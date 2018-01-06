# -*-coding:utf-8 -*-
import urllib2
import urllib




URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'


def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print('============response body=============')
    print(response.info())
    print('============response body=============')

    print ''.join([line for line in response.readlines()])

def use_params_urllib2():
    # 构建参数
    params = urllib.urlencode({'param1':'hello', 'param2':'world'})
    print('request params:')
    print(params)
    # 发送请求
    response = urllib2.urlopen('?'.join([URL_GET, "%s"])%params)
    # 相应处理
    print('============request header=============')
    print(response.info())
    print('============request header=============')
    print('status code ', response.getcode())
    print('============response body=============')
    print ''.join([line for line in response.readlines()])
    print('============response body=============')

if __name__ == '__main__':
    print('========simple urllib2 demo================')
    # use_simple_urllib2()

    print('========params urllib2 demo================')
    use_params_urllib2()