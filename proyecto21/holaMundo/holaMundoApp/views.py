from django.shortcuts import render
from holaMundoApp.models import Employee
from . import forms

# Create your views here.
def employeeData(request):
    empleados = Employee.objects.all()
    print('empleados dice: ', empleados)
    data = {'empleados': empleados}
    return render(request, 'holaMundoApp/empleados.html', data)

def userRegistrationView(request):
    form = forms.UserRegistrationForm()
    
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Form es Válido')
            print('Nombre: ', form.cleaned_data['nombre'])
            print('Email: ', form.cleaned_data['email'])
            print('Fono: ', form.cleaned_data['fono'])
            
    data = {'form':form}
    return render(request, 'holaMundoApp/userRegistration.html', data)

# Crear instancias del modelo Empleado.
    #empleado = Employee(nombre='Juanito', email='perez@gmail.com', fono='123456')
    #empleado.save()
    # Employee.objects.create(nombre='Pedrito', email='pato@gmail.com', fono='9999')
# Debería funcionar cualquiera de los 2.