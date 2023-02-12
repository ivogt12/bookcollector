from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name= 'about'),
    path('books/', views.BookList.as_view(), name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/create', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/add_review/', views.add_review, name='add_review'),
    path('books/<int:book_id>/assoc_award/<int:award_id>/', views.assoc_award, name='assoc_award'),
    path('books/<int:book_id>/disassoc_award/<int:award_id>/', views.disassoc_award, name='disassoc_award'),
    path('awards/', views.AwardList.as_view(), name='awards_index'),
    path('awards/<int:pk>/', views.AwardDetail.as_view(), name='awards_detail'),
    path('awards/create/', views.AwardCreate.as_view(), name='awards_create'),
    path('awards/<int:pk>/update/', views.AwardUpdate.as_view(), name='awards_update'),
    path('awards/<int:pk>/delete/', views.AwardDelete.as_view(), name='awards_delete'),
]
