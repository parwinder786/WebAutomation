import datetime
from datetime import datetime

# print("Hello, World!")
# ee = '"endDateTime":"2022-09-19T17:07:05.000Z"'
# ce = '2022-09-21T20:30:39.000Z'
# de = '"endDateTime":"2022-09-20T17:07:05.000Z"'
#
# ff = ce.split()
# print(ff)
# sss = ff[0][0:19]
# print(sss)
# x = sss.replace('T', ' ')
# print(x)
#
# d = datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
# print(d)
#
#
# ab = ee.split()
# cd = de.split()
#
#
# #e = ee.replace('T', ' ')
# #d = de.replace('T', ' ')
#
# print(ab)
# print(cd)
#
# edt = ab[0][15:34]
# sdt = cd[0][15:34]
#
# m = edt.replace('T', ' ')
# n = sdt.replace('T', ' ')
#
# print(m)
# print(n)
#
# d1 = datetime.strptime(m, "%Y-%m-%d %H:%M:%S")
# d2 = datetime.strptime(n, "%Y-%m-%d %H:%M:%S")
#
# diff = d2 - d1
# print(diff.days)


e = """ #            ____ _____ ____           _   _ ____  _____    _    ____          #

 #           |  _ \_   _/ ___|         | | | |  _ \| ____|  / \  |  _ \         #

 #           | |_) || || |      _____  | |_| | |_) |  _|   / _ \ | |_) |        #

 #           |  __/ | || |___  |_____| |  _  |  __/| |___ / ___ \|  __/         #

 #           |_|    |_| \____|         |_| |_|_|   |_____/_/   \_\_|            #

 #                                                                              #

 #  --------------------------------------------------------------------------  #

 #        Name ........ ptcmgmt-cn1259      User ........ root                  #

 #        OS .......... 8.2 (Ootpa)         SSH Logins .. 3                     #

 #        Config ...... 20220321            Uptime ...... 11d:1h:16m:24s        #

 #        Update ...... LVVR Update Success IP .......... 10.255.255.220 192.   #

 #        Pilot ....... No information                                          #

 #                                                                              #

 # ############################################################################ #

 # W A R N I N G  -  PRIVATE COMPUTER SYSTEM                                    #

 #  --------------------------------------------------------------------------  #

 # Use of CN's network and other information technology assets, including but   #

 # not limited to CN computers, servers, email, and Internet access, is         #

 # restricted to authorized CN personnel only and is governed by CN policies    #

 # and standards, including the CN Code of Business Conduct, Social Media       #

 # Policy and CN Information Security Policy. All information technology assets #

 # made available to and used by CN employees remain the Company’s sole         #

 # property. CN employees should have no expectation of privacy when using      #

 # them. Any data stored or transmitted on CN’s information technology assets   #

 # may be monitored, accessed or deleted by CN, without notice. Unauthorized    #

 # use of, or access to, CN's network and other information technology assets   #

 # may be subject to disciplinary action up to and including termination of     #

 # employment, denial of access to CN's information technology assets, criminal #

 # prosecution and other legal action.                                          #

 #                                                                              #

 # A V E R T I S S E M E N T  -  SYSTÈME INFORMATIQUE PRIVÉ                     #

 #  --------------------------------------------------------------------------  #

 # L’utilisation du réseau du CN et d’autres actifs informatiques, incluant les #

 # ordinateurs du CN, les serveurs, les courriels et l’accès Internet, est      #

 # limitée au personnel autorisé du CN et est régie par les politiques et       #

 # normes du CN, y compris le Code de conduite du CN, la Politique du CN        #

 # relative aux médias sociaux et la Politique de sécurité de l’information du  #

 # CN. Tous les actifs informatiques que le personnel du CN a à sa disposition  #

 # et utilise demeurent la propriété exclusive de la Compagnie. Les membres du  #

 # personnel du CN ne devraient avoir aucune expectative de vie privée dans le  #

 # cadre de leur utilisation. Toute donnée transmise au moyen des actifs        #

 # informatiques du CN ou stockée sur ceux-ci peut être surveillée, consultée   #

 # ou supprimée par le CN, sans préavis. Tout accès ou utilisation non-autorisé #

 # du réseau ou des autres actifs informatiques du CN peut donner lieu à des    #

 # mesures disciplinaires pouvant aller jusqu’au congédiement, au refus d’accès #

 # à l’actif informatique du CN, à des poursuites criminelles ou à d’autres     #

 # actions en justice.                                                          #

 # ############################################################################ #

tail -f /var/log/lvvragent/lvvragent.log | grep /data/medm/FileDrop 

[root@ptcmgmt-cn1259 ~]# tail -f /var/log/lvvragent/lvvragent.log | grep /data/me
edm/FileDrop 

[2022-09-26 18:56:22] [1733] [info] Directory '[01;31m[K/data/medm/FileDrop[m[K' created

[2022-09-26 18:56:22] [1733] [info] Permissions of directory '[01;31m[K/data/medm/FileDrop[m[K' changed

[2022-09-26 18:56:22] [1733] [info] File copied from /home/ftp/hpeapftp/6331f5d4351da63f160eb325/LSI_CN_0_20220925_1856_20220925_1857_6331f5d4351da63f160eb325.ldf to [01;31m[K/data/medm/FileDrop[m[K/LSI_CN_0_20220925_1856_20220925_1857_6331f5d4351da63f160eb325.ldf for request 6331f5d4351da63f160eb325

[2022-09-26 18:56:22] [1747] [info] [01;31m[K/data/medm/FileDrop[m[K/LSI_CN_0_20220925_1856_20220925_1857_6331f5d4351da63f160eb325.ldf has been added to timestamps

[2022-09-26 18:56:22] [1747] [info] Sent response on medm/response: {"appID":"app01","clientResp":{"media":{"accessClass":1,"color":"","compressed":false,"deviceID":"PowerView","encrypted":false,"endDateTime":"2022-09-25T18:57:19.000Z","extension":"ldf","filePath":"[01;31m[K/data/medm/FileDrop[m[K","filename":"LSI_CN_0_20220925_1856_20220925_1857_6331f5d4351da63f160eb325.ldf","integrityValidation":true,"location":null,"md5":"23f54cb050878461895f8c9432f15826","mimeType":"application/events","size":538,"startDateTime":"2022-09-25T18:56:19.000Z"}},"createdDt":"2022-09-26T18:56:19.000Z","edgeID":"ptcmgmt-cn1259","hostID":"host01","pckgCnt":1,"pckgId":1,"priority":1,"reason":"Requested","reqVersion":"1.0","requestID":"8b3bc6ff-a1e6-4f33-8c5b-6b433315c077","status":"GENERATED","statusDesc":"Success","statusDt":"2022-09-26T18:56:22.000Z","user":"17000"}"""

# print(len(e))
#
# #print(e[4051:5690])
# f = []
# a = []
# out = e.split('\n')
# #print(len(a))
# c = []
#
# for i in range(len(out)):
#     re = out[i]
#     a.append(re.strip())
# print(a)
# print(len(a))
# e = a[-3]
# print(e)
# #

# for i in range(len(a)):
#                 if a[i].__contains__('[root@ptcmgmt-cn1259 ~]# tail -f /var/log/lvvragent/lvvragent.log'):
#                     file = a[i]
# print(file)

# actual_result = ''
# if len(a) != 0:
#         for found in a:
#              if not found.__contains__('#####') and not found.__contains__('actions en justice'):
#                   actual_result = actual_result + '\n' + found
# print(actual_result)


# for i in range(len(a)):
#    if a[i].__contains__('tail -f /var/log/lvvragent/lvvragent.log | grep /data/medm/FileDrop'):
#       file = a[i]
# #print(file)
#
#
# for j in range(len(a)):
#    if a[j].__contains__('"user":"17000"}'):
#       file1 = a[j]
# #print(file1)
# #print(len(file1))
#
# sta = a.index(file)
# end = a.index(file1)
#
# com = a[sta:end]
# print(com)
numbers = [5, 3, 6, 70, 4, 2, 4, 3]
i = 0
square = 500
success = False
while i < len(numbers):
    if numbers[i] ** 2 > square:
        print(numbers[i], "squared is larger than", square)
        success = True
        break
    print(numbers[i], "squared is not larger than", square)
    i += 1
if not success:
    print("None were large enough!")

