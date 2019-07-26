# -*- coding:utf-8 -*-

import os
import json
import requests

# 翻译文本
def translate(content):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': content,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        result = json.loads(response.text)
        srcstr = result['translateResult'][0][0]['src']
        tgtstr = result['translateResult'][0][0]['tgt']
        print(u"{src} -> {tgt}".format(src=srcstr, tgt=tgtstr))
        return tgtstr
    else:
        print(u"有道词典调用失败")
        return None

# 分析文本内容
def analyzeText(content):
    # 获取'='的位置，若为-1表示不存在
    pos = content.find('=')
    if(pos != -1):
        # 存在的话，将等号左侧内容和右侧内容分别存储
        leftstr = content[0:pos]
        rightstr = content[pos+1:-1]
        newstr = leftstr + translate(rightstr)
        print(newstr)

# 读取文件
def readFile(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            content = line.strip()
            analyzeText(content)

if __name__ == '__main__':
    readFile('chinese.l')
