import socket
import time

file1 = open('ip.txt', 'r')
ips = file1.readlines()
for ip in ips:
    try:
        ip = ip.strip("\n")
        with open('ip_out.txt', 'a+') as file:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                result_code1 = s.connect_ex((ip, 80))
                if result_code1 == 0:
                    file.write('http://'+ip+'\n')
                else:
                    print(ip, 80, result_code1)
            except Exception as e:
                print e
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                result_code2 = s.connect_ex((ip, 443))
                if result_code2 == 0:
                    file.write('https://'+ip+'\n')
                else:
                    print(ip, 443, result_code2)
            except Exception as e:
                print e
            s.close()
    except Exception as e:
        print e
