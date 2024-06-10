# from coleta_armazena_mysql.views import LocalViewSet, PrevisaoViewSet
# from rest_framework import routers, permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
# Swagger Documentation
# schema_view = get_schema_view(
#     openapi.Info(
#         title="OpenWeatherMap | UFMS",
#         default_version='v1',
#         description="Sistema de disponibilização de dados via coleta e armazenamento remoto por meio da API da OpenWeatherMap.",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="kae.budke@gmail.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )


# # Rotas/Endpoints
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'localidades', LocalViewSet)
# router.register(r'previsoes', PrevisaoViewSet)

# Padrões de URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('coleta_armazena_mysql.urls'), name='coleta_armazena_mysql_urls')
]
