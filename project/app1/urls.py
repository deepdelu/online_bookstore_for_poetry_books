from django.urls import path, include
from app1 import views
urlpatterns =[
   path('',views.poetriesview.as_view()),
   path('home/',views.poetriesview.as_view()),
    path('base/',views.baseview.as_view()),
    path('poetries/',views.poetriesview.as_view()),
    path('form/',views.formview.as_view()),
    path('prod/',views.prodview.as_view()),
    path('about/',views.aboutview.as_view()),
    path('tsc/',views.tscview.as_view()),
    path('prcy/',views.prcyview.as_view()),
    path('cont/',views.contview.as_view()),
    path('ship/',views.shipview.as_view()),
    path('pay/',views.payview.as_view()),
    path('insertbase/',views.insertbase),
    path('insertform/',views.insertform),
    path('insertcont/',views.insertcont),

    path('login/', views.signin, name="signin"),
	path('logout/', views.signout, name="signout"),
	path('registration/', views.registration, name="registration"),
]