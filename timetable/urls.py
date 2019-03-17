import django
django.setup()

from timetable import views
from django.urls import path

urlpatterns = [
    path('', views.enter, name = 'enter'),
    path('start/', views.start, name = 'start'),
    path('setsubject/', views.setSubject, name ='setsub'),
    path('groups/', views.timetable_groups, name ='t_groups'),
    path('teachers/', views.timetable_prepod, name ='t_teachers'),
    path('auds/', views.timetable_aud, name ='t_aud'),
    path('delsubject/', views.delSubject, name ='delsub'),
    path('setting/', views.ChangePassword, name='change'),
    path('gost_timetable/', views.timetable_gost, name='enter_gost'),
    path('gost_teachers_timetable/', views.timetable_teachers_gost, name='enter_gost_teach'),
    path('gost_auds_timetable/', views.timetable_auds_gost, name='enter_gost_auds'),
    path('timetable/', views.timetable, name='timetable'),
    path('options/', views.options, name='options'),
    path('users_view/', views.users_view, name='users_view'),
    path('university_view/', views.users_view, name='university_view'),

    #path('first/', views.get_name, name ='name1'),

]
