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


#api6 대표임명_민경
#회원 이름의 경우 user.email로 구현
def appoint_user(request, id):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=id) #user 존재하지 않으면 404 에러 반환

        # 이미 대표가 있고, 현재 사용자가 대표가 아닌 경우 400 에러+메세지 반환
        if User.objects.filter(is_leader=True).exclude(pk=id).exists():
            return JsonResponse({"message": "대표는 2명 이상일 수 없습니다."}, status=400)
        
        #이미 대표일 경우 대표 자격 박탈
        if user.is_leader == True:
            user.is_leader = False
            user.save()
            return JsonResponse({"message": f"{user.email}(을)를 대표 자격을 박탈하였습니다."})
        else: 
            user.is_leader = True
            user.save()
            return JsonResponse({"message": f"{user.email}(을)를 대표로 임명 하였습니다."})
    
    else:
        return JsonResponse({'message': 'POST 요청만 허용됩니다.'})
    

#api7 모든정보조회_민경
def list_all(request):
    if request.method == 'GET':
        users = User.objects.all()
        total_hearts = sum(user.hearts for user in users)
        data = {
            "message" : "모든 회원들의 정보 (회원 수, 총 하트수) 입니다.",
            "member_count": users.count(),
            "total_hearts": total_hearts
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'GET 요청만 허용됩니다.'})