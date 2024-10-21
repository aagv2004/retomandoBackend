from django.shortcuts import render
from holaMundoApp.models import Employee

# Create your views here.
def employeeData(request):
    empleados = Employee.objects.all()
    print('empleados dice: ', empleados)
    data = {'empleados': empleados}
    return render(request, 'holaMundoApp/empleados.html', data)