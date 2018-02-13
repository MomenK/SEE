print "Populating Earth..."

import datetime

from django.db import models
from django.utils import timezone
import os
import sys
import django
import time
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charts.settings')
django.setup()

from charts.models import ECoG
from django.utils import timezone
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0
x8 = 0
x9 = 0
x10 = 0
select = 0


while True:
    time.sleep(1)


    x1 = x1+1
    x2 = random.randint(10,20)
    x3 = random.randint(10,20)
    x4 = random.randint(10,20)
    x5 = random.randint(10,20)
    x6 = random.randint(10,20)
    x7 = None
    x8 = None
    x9 = None
    x10 = None

    if select == 0:
        x7 = random.randint(10,200)
    elif select ==1:
        x8 = random.randint(10,200)
    elif select == 2:
        x9 = random.randint(10,200)
    elif select == 3:
        x10 = random.randint(0,200)
        select = -1
    select = select+1
    q = ECoG(Value1=x1,Value2=x2,Value3=x3,Value4=x4,Value5=x5,Value6=x6,Value7=x7,Value8=x8,Value9=x9,Value10=x10, Time=timezone.now())
    q.save()
    #print q.id
    print ECoG.objects.latest('id').id
    #queryset = ECoG.objects.all()
    #print([p.Time.strftime('%m/%d/%Y') for p in queryset])
    #print([str(p.Value) for p in queryset])





print "Never Reach me"
