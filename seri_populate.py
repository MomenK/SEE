#export DJANGO_SETTINGS_MODULE=charts.settings

print "Populating Earth with Serial..."


import datetime

from django.db import models
from django.utils import timezone
import os
import sys
import django
import time
import numpy as np


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charts.settings')
django.setup()

from charts.models import ECoG
from django.utils import timezone

i=0
word_count = 1
index = (word_count-1)*6
x =0


import serial

ser = serial.Serial('/dev/serial/by-id/usb-Texas_Instruments_XDS110__02.03.00.07__Embed_with_CMSIS-DAP_L1000912-if00', 115200, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False)

ser.flushInput()
ser.flushOutput()

# while True:
#     #print( ser.readline())
#     data_raw = ser.readline()[0:-2];
#     print(data_raw)
#     if(data_raw):
#         if (data_raw[0]=="[" and "[" not in data_raw[1:-1]):
#             data_raw = data_raw[1:-1]
#             print(data_raw[index :index +5])
#
#             x = int(data_raw[index :index +5].replace(" ",""),16)
#             print(x)
#             q = ECoG(Value1=x,Value2=x, Time=timezone.now())
#             q.save()
#             queryset = ECoG.objects.all

while True:
    #print( ser.readline())
    data_raw = ser.readline()[0:-2];
    data_bits = 336
    semantics = 3
    #print(data_raw)
    if (len(data_raw) > data_bits and len(data_raw) <= data_bits+ semantics) :
        #data_raw = data_raw[0:-1]
        #print(data_raw)
        #print(len(data_raw))
        check = data_raw[336:]
        #print(data_raw)
        n= 3*16
        data_listed= [data_raw [i:i+n] for i in range(0, len(data_raw ), n)]
        n =3
        x =[]
        #print(data_listed)
        for J in data_listed:
            x.append([J [i:i+n] for i in range(0, len(J), n)])
        y = np.asarray(x)
        # print("Fullubabe")
        # print(y)
        # print(len(y[0]))
        # print(y[0])
        # print(y[1])
        # print(y[2])
        # print(y[3])
        # print(y[4])
        # print(y[5])
        # print(y[6])
        #print(y[7])
        print(check)
        #select = y[7][0]
        for m in range(0,len(y[0])):
            aux1 = None
            aux2 = None
            aux3 = None
            aux4 = None
            select = (m+1)%4
            print(select)
        #for m in range(0,1):
            if select == 0:
                aux1 = int(y[6][m],16)
            elif select == 1:
                aux2 = int(y[6][m],16)
            elif select == 2:
                aux3 = int(y[6][m],16)
            elif select == 3:
                aux4 = int(y[6][m],16)
            print(y[0][m],y[1][m],y[2][m],y[3][m],y[4][m],y[5][m],aux1,aux2,aux3,aux4)
            #print(int(y[0][m],16),int(y[1][m],16),int(y[2][m],16),int(y[3][m],16),int(y[4][m],16),int(y[5][m],16),aux1,aux2,aux3,aux4)

            q = ECoG(Value1= int(y[0][m],16),Value2= int(y[1][m],16),Value3= int(y[2][m],16),Value4= int(y[3][m],16),Value5= int(y[4][m],16),Value6= int(y[5][m],16),Value7=aux1,Value8=aux2,Value9=aux3,Value10=aux4, Time=timezone.now())
            q.save()
        #print(select)
            #querint(yset = ECoG.objects.all()
        # if(data_raw):
        #     if (data_raw[0]=="[" and "[" not in data_raw[1:-1]):
        #         data_raw = data_raw[1:-1]
        #         print(data_raw[index :index +5])
        #
        #         x = int(data_raw[index :index +5].replace(" ",""),16)
        #         print(x)
        #         q = ECoG(Value1=x1,Value2=x2,Value3=x3,Value4=x4,Value5=x5,Value6=x6,Value7=x7,Value8=x8,Value9=x9,Value10=x10, Time=timezone.now())
        #         q.save()
        #         querint(yset = ECoG.objects.all()
