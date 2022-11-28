from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
]

admin.site.site_header = 'Админка'
