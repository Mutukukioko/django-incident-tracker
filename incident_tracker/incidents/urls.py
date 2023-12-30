# incidents/urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import IncidentList, IncidentDetail,IncidentListView

urlpatterns = [
    path('incidents/', IncidentList.as_view(), name='incident-list'),
    path('incidents/<int:pk>/', IncidentDetail.as_view(), name='incident-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('incidents-list/', IncidentListView.as_view(), name='incident-list-view'),
]