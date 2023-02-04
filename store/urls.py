from django.urls import path
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products',views.ProductViewSet,basename='products')
router.register('collections', views.CollectionViewSet)

proudct_router = routers.NestedDefaultRouter(router,'products',lookup='product')
proudct_router.register('reviews',views.ReviewViewSet, basename='proudct-reviews')
# URLConf
urlpatterns = router.urls + proudct_router.urls
