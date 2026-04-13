from django.urls import path
from .views import pipeline_view, move_deal_stage, move_deal_to_stage

urlpatterns = [
    path('pipeline/', pipeline_view, name='pipeline'),
    path('pipeline/deal/<int:deal_id>/<str:direction>/', move_deal_stage, name='move_deal_stage'),
    path('pipeline/deal/<int:deal_id>/move_to/<str:stage>/', move_deal_to_stage, name='move_deal_to_stage'),
]