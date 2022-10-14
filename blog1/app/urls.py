from.import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('hi/',views.hi),
    path('register/',views.register),
    path('login/',views.login),
    path('insert/',views.insert),
    path('blog/',views.blog),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),

    path('blog_detail/<int:id>/',views.blog_detail),

]

urlpatterns +=  staticfiles_urlpatterns()