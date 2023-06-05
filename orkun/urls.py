from django.urls import path
from orkun.views import HomeView, SingleProject

app_name = 'orkun'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('project/<int:pk>', SingleProject.as_view(), name='single-project'),
]