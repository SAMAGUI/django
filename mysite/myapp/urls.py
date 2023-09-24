from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = router.urls

urlpatterns += [
    # path('api/enterprise', EnterpriseAPIView.as_view())
]