from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from catalog import views


router = routers.DefaultRouter()
router.register(r'evidence', views.EvidenceViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('cases/', views.CaseEviView.as_view(), name = 'cases'),
    path('case/<int:pk>', views.CaseDetailView.as_view(), name='case-detail'),
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
