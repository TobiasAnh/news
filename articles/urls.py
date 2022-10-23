from django.urls import path

from articles.views import(
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
) 


urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name = "article_detail"),
    path("<int:pk>/", ArticleUpdateView.as_view(), name = "article_edit"),
    path("<int:pk>/", ArticleDeleteView.as_view(), name = "article_delete"),
    path("", ArticleListView.as_view(), name = "article_list"),
    ]