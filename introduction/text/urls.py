from django.contrib import admin
from django.urls import path
import text.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', text.views.home, name = "home"),
    path('profile/', text.views.profile, name = "profile"),
    path('future/', text.views.future, name = "future"),
]