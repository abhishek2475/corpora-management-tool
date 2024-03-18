# Necessary imports
from django.urls import path
from . import views

"""
URL patterns for the Corpus Manager application.

This module defines the URL patterns for the different views in the Corpus Manager application.
Each URL pattern is associated with a specific view function.

URL Patterns:
- "" (empty string): The index view.
- "home/": The home view.
- "add/": The add view.
- "deletion/": The deletion view.
- "home/delete/<int:id>/<int:choice>/": The delete view.
- "home/update/<int:id>/<int:choice>/": The update view.
- "upload/": The upload view.
- "api/parallel-texts/": The ParallelTextListCreate view.
- "signup/": The register view.
- "login/": The signin view.
- "logout/": The signout view.
"""

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("add/", views.add, name="add"),
    path('deletion/', views.deletion, name='deletion'),
    path('home/delete/<int:id>/<int:choice>/', views.delete, name='delete'),
    path('home/update/<int:id>/<int:choice>/', views.update, name='update'),
    path('upload/', views.upload, name='upload'),
    path('api/parallel-texts/', views.ParallelTextListCreate.as_view(), name='parallel-text-list-create'),
    path('signup/', views.register, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout')
]

