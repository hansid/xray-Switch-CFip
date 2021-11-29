import os,sys
import json
import csv
os.system('/root/cfip/CloudflareST -f /root/cfip/ip.txt -o /root/cfip/result.csv -t 1 -n 500')
print('\n\n'+"test end!"+'\n\n')
with open('/root/cfip/result.csv', 'r') as f:
	reader = csv.reader(f)
	result = list(reader)
	bestip = str(result[1]).split("'")[1]
	print('\n\n'+bestip+'\n\n')

json_path = '/root/xray/config.json'
f = open(json_path,'r+')
flist = f.readlines()
flist[79] = '                        "address": "'+bestip+'",\n'
f = open(json_path,'w+')
f.writelines(flist)
f.close()
#os.system('cat '+json_path)
os.system('systemctl restart xray.service')
os.system("sed -n 80p /root/xray/config.json")
print("finish")