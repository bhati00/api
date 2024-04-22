from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
    TokenRefreshView,)


urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]