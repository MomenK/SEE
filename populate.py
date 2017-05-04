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
x = 0
y = 0

while True:
    time.sleep(2)

    q = ECoG(Value1=x,Value2=y, Time=timezone.now())
    q.save()
    #print q.id
    x = random.randint(0,20)
    y = random.randint(10,100)
    print ECoG.objects.latest('id').id
    #queryset = ECoG.objects.all()
    #print([p.Time.strftime('%m/%d/%Y') for p in queryset])
    #print([str(p.Value) for p in queryset])





print "Never Reach me"
