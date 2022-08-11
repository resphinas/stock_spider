import requests
import re
import time
import random
s = requests.session()
import requests



flag = '11_28'
totalphrase = 0
list_ip  = []
with open('./ip池/ip_new.txt','r',encoding='utf-8') as file:
    content = file.readlines(

    )
    list_ip = [ i.replace('\n','') for i in content ]
print(list_ip)
print('ip 代理读取成功 按任意键进行操作')
input()
for num in range(4350):

    # 代理服务器
    proxyHost = "ip"
    proxyPort = "port"
    while True:
        try:
            ip_random = random.choice(list_ip)
            host = ip_random.split(':')[0]
            port = ip_random.split(':')[1]
            proxyMeta = "http://%(host)s:%(port)s" % {
                "host": host,
                "port": port,
            }
            time.sleep(5)
            print(proxyMeta)

            proxies = {                "http": proxyMeta,

            }
            res = s.get(f'http://guba.eastmoney.com/list,hk03396_{num+1}.html')
            print(res)

            if len(res.content)<50:
                print(f'{num} pages have done\n')

                input("check")
            break
        except :
            print('失效，正在重新调取，waiting............')
            continue

        pass
    # time.sleep(8)
    content = res.content.decode('utf8', 'ignore')
    print(content)
    list0 = re.findall(f'title="(.*?)">.*?</a></span>', content)
    list1 = re.findall(f'<span class="l5 a5">(.*?)</span>', content)[1:]
    print(f'{num} pages have done\n'+ f'last data = {flag}')
    apage_content = ''
    for i in range(len(list1)):
        totalphrase +=1
        try:
            print(flag,list0[i])

            # list2.append(list1[i][:5].replace('-','_')+' ' + list0[i])
            flag_current = list1[i][:5].replace('-','_')
            if flag_current != flag:
                flag = flag_current
                continue
            apage_content += list0[i] + '\n'
        except:

            pass
        with open(flag + '.txt', 'a+', encoding='gbk', errors='ignore') as file:
            file.write(apage_content)



print(list2)
print(len(list2))