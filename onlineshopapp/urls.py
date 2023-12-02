from django.urls import include, path
from .views import CategoryDetailView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/<uuid:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]