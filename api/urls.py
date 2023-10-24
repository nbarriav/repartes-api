from django.urls import path, include
from .views import (
    ClientView,
    QuoteView,
    GroceryView,
    QuoteDetailsView,
    ShopperView,
    QuoteAssignmentView,
    RouteAssignmentView,
)
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("clients/", ClientView.as_view()),
    path("quotes/", QuoteView.as_view()),
    path("groceries/", GroceryView.as_view()),
    path("quotes/<int:pk>/", QuoteDetailsView.as_view()),
    path("shoppers/", ShopperView.as_view()),
    path("quotes/assign/", QuoteAssignmentView.as_view()),
    path("routes/", RouteAssignmentView.as_view()),
]
