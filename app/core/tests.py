#from django.test import TestCase
from app.wsgi import *
from core.models import Type, Employee

#Listar
#query = Type.objects.all()
#print(query)

#Insertar
#t = Type()
#t.name = 'Presidente'
#t.save()

#edicion

#try:
#    t = Type.objects.get(pk=2)
#    t.name = 'Dibujante'
#    t.save()
#except Exception as e:
#    print(e)

#eliminacion
#t = Type.objects.get(pk=1)
#t.delete()

#Employee.objects.filter()

#obj = Type.objects.filter(name__contains='Dib').count()
#print(obj)

