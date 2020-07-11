from django.http import JsonResponse

def profile(request):
    data = {
        'name': 'Ava',
      	'age': 21
    }
    return JsonResponse(data)