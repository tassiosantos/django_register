from register_versao1 import views
from django.conf.urls import url

urlpatterns = [
    url(r'^cadastro/', views.cadastro,name='cadastro'),
    url(r'^login/', views.index,name='index'),
]
