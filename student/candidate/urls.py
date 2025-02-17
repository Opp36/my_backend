from django.urls import path
from candidate.views import info, activity

urlpatterns = [
    path('all/', info, name='info'),
    path('act/', activity, name='activity'),
]