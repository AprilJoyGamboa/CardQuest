from django.urls import path
from cardquest import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', views.TrainerListView.as_view(), name='trainer_list'),
    path('collection_list', views.CollectionListView.as_view(), name='collection_list'),
    path('pokemon_card', views.PokemonCardListView.as_view(), name='pokemon_card'),
]