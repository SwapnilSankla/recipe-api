from django.urls import path, include

from user.views import CreateUserView, CreateTokenView, ManageUserView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('me/', ManageUserView.as_view(), name='me'),
    path('token/', CreateTokenView.as_view(), name='token'),
]
