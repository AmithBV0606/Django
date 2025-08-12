from django.http import  HttpResponse
from django.shortcuts import render, get_object_or_404
from employees.models import Employee

# Create your views here.


def employee_details(request, pk):
    # print(pk)
    # try:
    #     employee = Employee.objects.get(pk=pk)
    #     print(employee)
    #     # context = {
    #     #     'employee': employee
    #     # }
    #     # return render(request, 'home.html', context)
    # except:
    #     raise Http404

    employee = get_object_or_404(Employee, pk=pk)
    return HttpResponse(employee)