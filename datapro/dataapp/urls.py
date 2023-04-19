from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'master', views.Rsm,basename='master'),

urlpatterns = [
    path('monitor/', views.joins, name='joined'),
    path('latest_data_retrival/', views.DataAnalysis.as_view(), name='retrival'),
    path('ins_retrival/', views.InstantData.as_view(), name='ins_retrival'),
    path('retrieve/<str:table_code>/<str:date_from>/<str:date_to>/<str:meter>/<str:col_code>/', views.Retrieve, name='retrieve'),
    path('meterId_ser_num/', views.Meter_Retrieve.as_view(),name='meterId_ser_num'),
    path('description/<str:table_code>/', views.description,name='description'),
    path('table_des/', views.Table_desc.as_view(), name='table_des'),
    path('ins/', views.Ins.as_view(), name='ins'),
    path('block/', views.Block.as_view(), name='block'),
    path('daily/', views.Daily.as_view(), name='daily'),
    path('', include(router.urls)),
    path('process/',views.Profile.as_view(),name='process'),
]
