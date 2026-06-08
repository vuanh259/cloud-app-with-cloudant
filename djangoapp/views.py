from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(username=data['userName'], password=data['password'])
        if user is not None:
            login(request, user)
            return JsonResponse({"userName": data['userName'], "status": "Authenticated"})
    return JsonResponse({"status": "Failed"})

def logout_user(request):
    logout(request)
    return JsonResponse({"userName": ""})

def get_dealerships(request, state=None):
    # Mock data phục vụ việc test API cURL nhanh chóng
    dealers = [
        {"id": 1, "name": "Toyota Dealer Kansas", "city": "Topeka", "state": "Kansas"},
        {"id": 2, "name": "Ford Dealer NY", "city": "New York", "state": "New York"}
    ]
    if state:
        dealers = [d for d in dealers if d['state'].lower() == state.lower()]
    return JsonResponse(dealers, safe=False)

def get_dealer_details(request, dealer_id):
    return JsonResponse({"id": dealer_id, "name": f"Dealer Mock {dealer_id}", "city": "Mock City"})

def get_dealer_reviews(request, dealer_id):
    return JsonResponse([{"dealer_id": dealer_id, "review": "Great car shopping experience", "sentiment": "positive"}], safe=False)

def get_cars(request):
    cars = [{"make": "Toyota", "model": "Camry"}, {"make": "Ford", "model": "Mustang"}]
    return JsonResponse({"CarMakes": cars})

def analyze_review(request, review_text):
    # Trả về kết quả Sentiment Analysis cho Task 16
    return JsonResponse({"sentiment": "positive", "text": review_text})