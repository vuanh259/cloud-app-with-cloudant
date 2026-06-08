from django.urls import path
from . import views

# Khai báo cấu trúc định tuyến cho ứng dụng con
app_name = 'djangoapp'
urlpatterns = [
    # API phục vụ Đăng nhập / Đăng xuất tài khoản
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    
    # API lấy danh sách và lọc Đại lý (Dealers)
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),
    
    # API lấy danh sách Đánh giá (Reviews) của Đại lý
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='get_dealer_reviews'),
    
    # API lấy thông tin Hãng xe / Dòng xe (Car Makes & Models)
    path('get_cars', views.get_cars, name='get_cars'),
    
    # API Phân tích cảm xúc văn bản đánh giá (Sentiment Analysis)
    path('analyze/<str:review_text>', views.analyze_review, name='analyze_review'),
]