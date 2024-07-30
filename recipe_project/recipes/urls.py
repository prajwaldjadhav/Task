from django.urls import path
from . import views

urlpatterns = [
    # API URLs
    path('api/recipes/', views.RecipeListCreate.as_view(), name='recipe-list-create'),
    path('api/recipes/<int:pk>/', views.RecipeRetrieveUpdateDestroy.as_view(), name='recipe-retrieve-update-destroy'),

    # Front-end URLs
    path('', views.recipe_list, name='recipe-list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe-detail'),
    path('recipe/new/', views.recipe_create, name='recipe-create'),
    path('recipe/<int:pk>/edit/', views.recipe_update, name='recipe-update'),
    path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe-delete'),
]