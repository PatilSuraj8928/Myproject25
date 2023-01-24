from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_Dept(request):
    tn=int(input('Enter the ID: '))
    sn=input('Enter the dept name: ')
    rn=int(input('Enter the no of employees: '))
    T=Dept.objects.get_or_create(ID=tn,dname=sn,empno=rn)[0]
    
    T.save()
    return HttpResponse('Data is inserted successfully')
    

def insert_emp(request):
    tn=int(input('Enter the ID: '))
    sn=input('Enter the dept name: ')
    rn=int(input('Enter the no of employees: '))
    T=Dept.objects.get_or_create(ID=tn,dname=sn,empno=rn)[0]
    
    w=int(input('enter the emlpoyee ID: '))
    s=int(input('Enter the MGR: '))
    r=input('Enter name of employee: ')
    p=int(input('Enter salary: '))
    d=input('enter the date: ')
    pos=input('Enter the position : ')

    E=Emp.objects.get_or_create(EID=w,MGR=s,ENAME=r,deptno=T,sal=p,hiredate=d,position=pos)[0]
    E.save()

    return HttpResponse('Data inserted in Emp table!!!')
   
