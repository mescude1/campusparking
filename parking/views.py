from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Propietario  # Asegúrate de importar el modelo Propietario

@login_required
def perfil(request):
    # Obtén el usuario autenticado
    user = request.user

    # Obtén el objeto Propietario asociado al usuario
    try:
        propietario = Propietario.objects.get(user=user)
    except Propietario.DoesNotExist:
        # Si no existe un objeto Propietario, redirige o muestra un mensaje de error
        propietario = None

    # Pasa los datos a la plantilla
    context = {
        'user': user,
        'propietario': propietario,
    }
    return render(request, 'parking/perfil.html', context)