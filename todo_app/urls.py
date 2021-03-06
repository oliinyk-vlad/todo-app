from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

from rest_framework import routers

from core.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),
]
