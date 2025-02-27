from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
# from .views import RegisterViewSet,LoginView,CategoryViewSet
from rest_framework.routers import SimpleRouter
from .views import*

schema_view = get_schema_view(
    openapi.Info(
        title="User Registration API",
        default_version="v1",
        description="API for user registration",
        contact=openapi.Contact(email="contact@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = SimpleRouter()
router.register(r"register", RegisterViewSet, basename="register"),
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("login/", LoginView.as_view(), name="login"),
    path("category/name/<str:name>/", CategoryByNameView.as_view(), name="category-by-name"),  # New URL
    path("products/category/<str:category_name>/", ProductByCategoryView.as_view(), name="products-by-category"),


]
