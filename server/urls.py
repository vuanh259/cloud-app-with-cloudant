from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Đường dẫn vào trang quản trị Admin
    path('admin/', admin.site.shape if hasattr(admin.site, 'shape') else admin.site.urls),
    
    # Kết nối các endpoints API từ ứng dụng djangoapp vào hệ thống
    path('djangoapp/', include('djangoapp.urls')),
    
    # Định tuyến mặc định cho Frontend React (Trang chủ)
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
]