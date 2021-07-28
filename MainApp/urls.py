from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('blocks/<slug:block_slug>', views.detail, name='block-detail')
    # path('blocks/<int:height>/', views.BlockDetailView.as_view(), name='block-detail')
]

