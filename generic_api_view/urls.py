
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # api with separate mixins
    # path('studentapi/',views.StudentList.as_view()),
    # path('studentapi/',views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrive.as_view()),
    # path('studentapi/<int:pk>/',views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentDelete.as_view()),

    path('studentapi/',views.LCStudentApi.as_view()),
    path('studentapi/<int:pk>/',views.RUDStudentApi.as_view()),

    # concrete view
    path('student_list/',views.StudentList.as_view()),
    path('student_create/',views.StudentCreate.as_view()),
    path('student_retrieve/<int:pk>/',views.StudentRetrieve.as_view()),
    path('student_update/<int:pk>/',views.StudentUpdate.as_view()),
    path('student_delete/<int:pk>/',views.StudentDelete.as_view()),
    path('student_lc/',views.StudentLC.as_view()),
    path('student_ru/<int:pk>/',views.StudentRU.as_view()),
    path('student_rd/<int:pk>/',views.StudentRD.as_view()),
    path('student_rud/<int:pk>/',views.StudentRUD.as_view()),
]
