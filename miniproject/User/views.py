import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import *

def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        email = data.get('email')
        password = data.get('password')
        is_leader = data.get('is_leader')
        hearts = data.get('hearts')

        user = User(
            email = email,
            password = password,
            is_leader = is_leader,
            hearts = hearts
        )
        
        user.save()
        return JsonResponse({'message' : 'success'})
    return JsonResponse({'message' : 'POST 요청만 허용됩니다.'})


def get_user(request,id):
    if request.method == 'GET':
        user = get_object_or_404(User, id = id)
        data = {
            'id' : user.id,
            'email' : user.email,
            'is_leader' : user.is_leader,
            'hearts' : user.hearts,
        }
        return JsonResponse(data, status = 200)
    else:
        return JsonResponse({'message': 'GET 요청만 허용됩니다.'})

def delete_user(request, id):
    if request.method == 'DELETE':
        user =get_object_or_404(User, id = id)
        user.delete()
        data = {
            "message" : f"id: {id}유저 삭제 완료"
        }
        return JsonResponse(data, status = 200)
    
    return JsonResponse({"message" : "DELETE 요청만 허용됩니다."})
