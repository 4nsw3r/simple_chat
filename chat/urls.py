from django.contrib import admin
#from django.contrib.auth import views as auth_views
from django.urls import path, include

from chat.views import ChatView, HomeView, MessagesAPIView, SearchView, Subscribe

from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('chat/<slug:chatname>/', ChatView.as_view(), name='chat'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/messages/<slug:chatname>/', MessagesAPIView.as_view(), name="messages"),
    path('admin/', admin.site.urls),
    path('accounts/register/', RegistrationView.as_view(success_url='/'), name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('results/', SearchView.as_view(), name='search'),
    path('addbl/<int:user_id>', Subscribe.as_view(), name='block')
]
