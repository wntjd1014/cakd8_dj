# homepage의 url에서 아무것도 없다면 (링크 들어가서 바로 뜨는 창에서)
#  views의 landing으로 처리해줘라.

from django.urls import path
from . import views

# 링크에서 about_me/ 로 들어오면 만들어둔 about_me로 반환해라.
urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
]
