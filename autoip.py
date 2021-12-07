
import os,sys
import json
import csv
os.system('/root/cfip/CloudflareST -f /root/cfip/ip.txt -o /root/cfip/result.csv -t 1 -n 500')
#/root/cfip/是测速程序放置的文件夹，cf测速的项目地址:https://github.com/XIU2/CloudflareSpeedTest
print('\n\n'+"test end!"+'\n\n')
#测速完后读取文件，提取最快的ip，变量名为bestip
with open('/root/cfip/result.csv', 'r',encoding='utf-8') as f:
	reader = csv.reader(f)
	result = list(reader)
	bestip = str(result[1]).split("'")[1]
	print('\n\n'+bestip+'\n\n')

json_path = '/root/xray/config.json'
#json_path是xray的配置文件config.json的位置
f = open(json_path,'r+',encoding='utf-8')
flist = f.readlines()
flist[79] = '                        "address": "'+bestip+'",\n'
#79是指行数，从0开始计数，按实际更改。
f = open(json_path,'w+',encoding='utf-8')
f.writelines(flist)
f.close()
#os.system('cat '+json_path)
os.system('systemctl restart xray.service')
#上面命令是指重启加载xray，根据自己实际更改
os.system("sed -n 80p /root/xray/config.json")
#这个是展示更改后的ip地址。
print("finish")
