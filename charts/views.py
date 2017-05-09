from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import get_user_model
from charts.models import ECoG

User = get_user_model()
sent_id = 0; #How to dynaically pass this shit?

class HomeView(View):
    def get(self, request, *args, **kwargs):
        global sent_id
        if request.method == 'GET' and 'Text' in request.GET:
            temp = request.GET['Text']
            print(int(temp) )
            sent_id = sent_id - int(temp)
        else:
            sent_id = 0;
        return render(request, 'charts.html', {})

def get_data(request, *args, **kwargs):
    data = {
        "sales":100,
        "customers":10,
    }
    return JsonResponse(data) #http request

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        global sent_id
        new_id = ECoG.objects.latest('id').id;
        if(sent_id != new_id):
            queryset = ECoG.objects.filter(id__range=(sent_id+1,new_id))
            print([p.Time for p in queryset])
            #print([p.Value for p in queryset])

            time = ([p.Time.strftime('%m/%d:%H:%M:%S') for p in queryset])
            value1 = ([str(p.Value1) for p in queryset])
            value2 = ([str(p.Value2) for p in queryset])
            sent_id = new_id;
            data = {
                "time":time,
                "value1":value1,
                "value2":value2,

            }
            return Response(data)
        return 0
