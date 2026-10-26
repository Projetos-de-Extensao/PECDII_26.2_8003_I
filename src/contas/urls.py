from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from contas.views import MeView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('me/', MeView.as_view(), name='me'),
]
