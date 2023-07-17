from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import ItemViewSet, OrderViewSet, category_list, tags_list


router = SimpleRouter()
router.register(r'products',ItemViewSet)
router.register(r'orders', OrderViewSet)


simple_url = [
    path('category_list/', category_list),
    path('tags_list/', tags_list)
]



urlpatterns = router.urls
urlpatterns += simple_url



