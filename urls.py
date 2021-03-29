from django.contrib import admin
from django.urls import path
from food.views import index,index1,index2,index3,index4,index5,view_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index,name='template1'),
    path('new/',index1,name='template2'),
    path('searchfood/',index2,name='template3'),
    path('searchall/',view_all,name='template4'),
    path('filter/',index3,name='template5'),
    path('abstract/',index4,name='template6'),
    path('teammembers',index5,name='template7'),
]
