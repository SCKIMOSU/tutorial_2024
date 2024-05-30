from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views



urlpatterns = [

    path('api-auth/', include('rest_framework.urls')),

    path('fbv_snippets/', views.snippet_list),
    path('fbv_snippets/<int:pk>/', views.snippet_detail),

    path('cbv_snippets/', views.SnippetList.as_view()),
    path('cbv_snippets/<int:pk>/', views.SnippetDetail.as_view()),

    path('mixins_snippets/', views.SnippetListMixins.as_view()),
    path('mixins_snippets/<int:pk>/', views.SnippetDetailMixins.as_view()),

    path('generics_snippets/', views.SnippetListGenerics.as_view()),
    path('generics_snippets/<int:pk>/', views.SnippetDetailGenerics.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)