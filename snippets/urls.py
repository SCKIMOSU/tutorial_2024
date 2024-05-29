from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path, include


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('snippets/', views.SnippetList.as_view()),  # 3rd code CBV URL
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()), # 3rd code CBV URL
    #path('snippets/', views.snippet_list), # FBV URL
    #path('snippets/<int:pk>/', views.snippet_detail), # FBV URL
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]


urlpatterns = format_suffix_patterns(urlpatterns)