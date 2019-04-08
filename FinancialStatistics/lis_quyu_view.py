from django.shortcuts import render
from django.http import HttpResponse
from FinancialStatistics.models_lis_quyu import View_1
from django.core import serializers

def lis_quyu_View_1(request):
    temp = View_1.objects.using('lis_quyu').all()
    # temp = View_1.objects.filter(buy_name="xxx")
    data = serializers.serialize("json",temp)
    return HttpResponse(data)