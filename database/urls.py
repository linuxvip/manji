# # FBV
# from django.urls import path
# from .views import database_info
#
# urlpatterns = [
#     path('', database_info, name='database_view'),
# ]




# CBV
from django.urls import path
from .views import DatabaseView

urlpatterns = [
    path('', DatabaseView.as_view(), name='database_view'),
    path('<int:pk>/', DatabaseView.as_view(), name='database_view'),
]

