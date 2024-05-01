from django.urls import path
from . import views


urlpatterns=[path('afficherCours', views.afficherCours),
             path('saveCours', views.saveCours)
]