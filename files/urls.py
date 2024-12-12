from django.urls import path
from .views import FileUploadView, FileSearchView, FileDeleteView, FileUpdateView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('search/', FileSearchView.as_view(), name='file-search'),
    path('delete/<int:id>/', FileDeleteView.as_view(), name='file-delete'),
    path('update/<int:id>/', FileUpdateView.as_view(), name='file-update'),  # New endpoint for updating
]
