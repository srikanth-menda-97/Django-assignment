from django.urls import path
from . import views

urlpatterns=[
	path('<int:candidate_id>/', views.index, name='index'),
]
