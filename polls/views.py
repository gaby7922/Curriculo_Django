from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    data = {}
    data['personal'] = {"name": "Gaby",
                        "lastname": "Hernandez"}
    data['address'] = {"home": "Ramon Laval 1638, La Reina"}

    data['abilities'] = {"programming_languages":['Python',' Php'],
                        "marking_language":"JavaScript, Html4, CSS",
                        "Framework":"Django","Methodologies":" Metodologías ágiles, Scrum", 
                        "additional":"Analista y Programador de Sistemas Web,Líder de Proyecto", 
                        "database":"Manejo y Administración de Bases de Datos PostgresSQL,  sql",
                        "others":"Elaboración de Casos de Uso,Administración y Desarrollo de Plataformas Distribuidas, Experiencia en el area del analisis"}
    
    return render(request, 'index.html', data)