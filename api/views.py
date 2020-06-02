from django.shortcuts import render
from django.http import HttpResponse
from .models import Group, Contact
from .serializers import GroupSerializer, ContactSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
def sendmail(request, format=None):
    data = request.data
    if 'templateID' in data:
        template = render_to_string(getTemplate(data['templateID']))
    else:
        template = ""
    send_mail('Test send mail', data['message'], data['from'], [data['to']], html_message=template)
    return Response({'detail': "send mail success"})

@api_view(['POST'])
def calculate_tax(request, format=None):
    net_income = request.data['net_income']
    tax = calculateTax(net_income)
    return Response({'tax': tax})

def getTemplate(id):
    if id == 1:
        return 'email_template.html'
    elif id == 2 : 
        return 'email_template_2.html'
    else:
        return ""

def calculateTax(net_income):
    if net_income <= 150000:
        rate_tax = 150000
        percent_tax = 0
        base_tax = 0
    elif net_income > 150000 & net_income <= 300000:
        rate_tax = 150000
        percent_tax = 5
        base_tax = 0
    elif net_income > 300000 & net_income <= 500000:
        rate_tax = 300000
        percent_tax = 10
        base_tax = 7500
    elif net_income > 500000 & net_income <= 750000:
        rate_tax = 500000
        percent_tax = 15
        base_tax = 27500
    elif net_income > 750000 & net_income <= 1000000:
        rate_tax = 750000
        percent_tax = 20
        base_tax = 65000
    elif net_income > 1000000 & net_income <= 2000000:
        rate_tax = 1000000
        percent_tax = 25
        base_tax = 115000
    elif net_income > 2000000 & net_income <= 5000000:
        rate_tax = 2000000
        percent_tax = 30
        base_tax = 365000
    elif net_income > 5000000 :
        rate_tax = 5000000
        percent_tax = 35
        base_tax = 1265000
    tax = ((net_income-rate_tax)*percent_tax/100)+base_tax
    if tax < 0:
        return 0
    else:
        return tax