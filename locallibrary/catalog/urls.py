from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from catalog import views


router = routers.DefaultRouter()
router.register(r'evidences', views.EvidenceViewSet)

router_case = routers.DefaultRouter()
router_case.register(r'case', views.EviCaseViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('cases/', views.CaseEviView.as_view(), name = 'cases'),
    path('case/<int:pk>', views.CaseDetailView.as_view(), name='case-detail'),
    url(r'^api/', include(router.urls)),
    url(r'^api-case/', include(router_case.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    
    path('evidences/', views.EvidenceView.as_view(), name = 'evidences'),
    path('evidence/<int:pk>', views.EvidenceDetailView.as_view(), name='evidence-detail'),
    ]