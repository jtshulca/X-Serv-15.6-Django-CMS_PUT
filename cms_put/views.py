from django.shortcuts import render
from django.http import HttpResponse
from cms_put.models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def show(request):
    record = Pages.objects.all()
    respuesta = "Pages Found: "
    for page in record:
        respuesta += "<li>/" + page.name + " --> " + page.page
    return HttpResponse(respuesta)
    
@csrf_exempt
def show_content(request, resource):
    if request.method == "GET":
        try:
            page = Pages.objects.get(name=resource)
            return HttpResponse(page.page)
        except Pages.DoesNotExist:
            respuesta = "Page not found, add: "
            respuesta += '<form action="" method="POST">'
            respuesta += "Nombre: <input type='text' name='nombre'>"
            respuesta += "<br>Página: <input type='text' name='page'>"
            respuesta += "<input type='submit' value='Enviar'></form>"
    elif request.method == "POST" or request.method == "PUT":
        nombre = request.POST['nombre']
        page = request.POST['page']
        pagina = Pages(name=nombre, page=page)
        pagina.save()
        respuesta = "Saved page: /" + nombre + " --> " + page
    return HttpResponse(respuesta)
