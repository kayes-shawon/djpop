from django.urls import path

from testify.views import HeadAPIView

urlpatterns = [
    path('internal/v1/head', HeadAPIView.as_view(), name="internal-v1-head")
]
