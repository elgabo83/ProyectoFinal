from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import index, ropa_masculina, ropa_femenina, eventos, camisas, camperas, hoodies, pantalones, remeras, shorts, zapatillas,botasf,zapatillasf,blusas,vestidos,faldas,pantalonesf,shortsf,camperasf,lanzamientos,galerias,delete_image




urlpatterns = [
    path('', views.index, name='index'),
    path('ropa-masculina/', views.ropa_masculina, name='ropa-masculina'),
    path('ropa-femenina/', views.ropa_femenina, name='ropa-femenina'),
    path('eventos/', views.eventos, name='eventos'),
    path('ropa-masculina/botas/', views.botas, name='botas'),  
    path('ropa-masculina/camisas/', views.camisas, name='camisas'),  
    path('ropa-masculina/camperas/', views.camperas, name='camperas'),  
    path('ropa-masculina/hoodies/', views.hoodies, name='hoodies'),  
    path('ropa-masculina/pantalones/', views.pantalones, name='pantalones'),  
    path('ropa-masculina/remeras/', views.remeras, name='remeras'),  
    path('ropa-masculina/shorts/', views.shorts, name='shorts'),  
    path('ropa-masculina/zapatillas/', views.zapatillas, name='zapatillas'),  

    path('ropa-femenina/botasf/', views.botasf, name='botasf'), 
    path('ropa-femenina/zapatillasf/', views.zapatillasf, name='zapatillasf'),  
    path('ropa-femenina/blusas/', views.blusas, name='blusas'),  
    path('ropa-femenina/vestidos/', views.vestidos, name='vestidos'),  
    path('ropa-femenina/faldas/', views.faldas, name='faldas'),  
    path('ropa-femenina/pantalonesf/', views.pantalonesf, name='pantalonesf'),  
    path('ropa-femenina/shortsf/', views.shortsf, name='shortsf'),  
    path('ropa-femenina/camperasf/', views.camperasf, name='camperasf'),  

    path('eventos/lanzamientos/', views.lanzamientos, name='lanzamientos'),  
    path('eventos/galerias/', views.galerias, name='galerias'),  

    
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),

    path('logout/', views.user_logout, name='logout'),
    path('upload/', views.upload_image_view, name='upload_image_view'),
    path('delete-image/<int:pk>/', delete_image, name='delete_image'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)