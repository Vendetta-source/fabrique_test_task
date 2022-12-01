from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from client.views import ClientViewSet
from mailing_list.views import MailingListViewSet
from message.views import MessageViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'message', MessageViewSet, basename='message')
router.register(r'mailings_list', MailingListViewSet, basename='mailings_list')
router.register(r'clients', ClientViewSet, basename='clients')

schema_view = get_schema_view(
   openapi.Info(
      title="Notification Service API",
      default_version='v1',
      description="Documentation for test task for Fabrika Resheniy.",
      contact=openapi.Contact(email="tamer.kab@mail.ru"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
