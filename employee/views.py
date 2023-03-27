from django.shortcuts import render

def EmpView(request):
    return render(request,"employee/index.html")
