from django.urls import path, include

from . import views 

urlpatterns =[
    path('', views.index , name = 'index'),
    path('accounts/', include('accounts.urls') ),
    # path('mj/', include('MJ.urls') ),
    path('feedback/', views.feedback, name = 'feedback'),
    path('menu/', views.menu, name = 'menu')
    # path("logout/",views.logout, name='logout'),
    
    
] 

# urlpatterns = urlpatterns+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)