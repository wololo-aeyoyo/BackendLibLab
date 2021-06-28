from rest_framework.response import Response
from .models import usuarios,puntuacion,creditos
from .serializers import creditosSerializer,usuariosSerializer,puntuacionSerializer
from rest_framework.decorators import api_view


# Create your views here.

#vistas creditos
@api_view(['GET'])
def allCredit(request):
    allCreditos = creditos.objects.all()
    serializers = creditosSerializer(allCreditos,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def oneCreditbyid(request,ids):
    unCreditos = creditos.objects.get(id=ids)
    serializers = creditosSerializer(unCreditos,many=False)
    return Response(serializers.data)


@api_view(['POST'])
def CrearCredito(request):
    serializer = creditosSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateCredito(request,ids):
    unCreditos = creditos.objects.get(id=ids)
    serializer = creditosSerializer(instance=unCreditos ,data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def deleteCredito(request,ids):
    unCreditos = creditos.objects.get(id=ids)
    unCreditos.delete()
    return Response("eliminado")

#vista para usuario

@api_view(['GET'])
def userData(request,ids):
    user = usuarios.objects.get(id=ids)
    serializers = usuariosSerializer(user,many=False)
    return Response(serializers.data)

#vista para puntuacion

@api_view(['GET'])
def allpuntacion(request):
    allpuntuacion = puntuacion.objects.all()
    serializers = puntuacionSerializer(allpuntuacion,many=True)
    return Response(serializers.data)
