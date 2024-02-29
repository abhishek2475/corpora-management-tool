from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('upload/', views.upload, name='upload'),
    path('api/parallel-texts/', views.ParallelTextListCreate.as_view(), name='parallel-text-list-create'),
    path('parallel-texts/', views.parallel_texts, name='parallel_texts'),
    path('signup/', views.register, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout')
]