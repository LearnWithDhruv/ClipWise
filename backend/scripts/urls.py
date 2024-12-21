from django.urls import path
from .views import GenerateScriptAPIView

urlpatterns = [
    path('generate/', GenerateScriptAPIView.as_view(), name='generate-script'),
]
