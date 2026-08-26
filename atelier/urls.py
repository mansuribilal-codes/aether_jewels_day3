from django.urls import path
from . import views

app_name = 'atelier'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('collections/', views.collection_list_view, name='collections'),
    path('collections/<slug:slug>/', views.collection_detail_view, name='collection_detail'),
    path('jewels/', views.product_list_view, name='product_list'),
    path('jewels/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('bespoke-atelier/', views.bespoke_configurator_view, name='bespoke'),
    path('book-consultation/', views.consultation_view, name='consultation'),
    path('heritage/', views.heritage_view, name='heritage'),
    path('journal/', views.journal_list_view, name='journal'),
    path('journal/<slug:slug>/', views.journal_detail_view, name='journal_detail'),
    path('vault/', views.vault_wishlist_view, name='vault'),
    path('developer/', views.developer_view, name='developer'),
    
    # User Authentication URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # API endpoints
    path('api/consultation/book/', views.api_consultation_book, name='api_consultation_book'),
    path('api/bespoke/inquire/', views.api_bespoke_inquire, name='api_bespoke_inquire'),
    path('api/products/<int:product_id>/quickview/', views.api_product_quickview, name='api_product_quickview'),
]
