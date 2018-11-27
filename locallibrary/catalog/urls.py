from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cases/', views.CaseEviView.as_view(), name = 'cases'),
    path('case/<int:pk>', views.CaseDetailView.as_view(), name='case-detail'),
    ]
