from django.urls import path
from django.contrib.auth import views as v
from Travelling import views

urlpatterns = [
	
	path('',views.home,name="hm"),
    path('register/',views.register,name="rg"),
    path('login/',v.LoginView.as_view(template_name="ta/login.html"),name="log"),
    path('profile/',views.pfle,name="pf"),
    path('update/',views.updf,name="upfe"),
    path('dashbord/',views.dashbord,name="dsh"),
    path('bus_search/',views.bus_search),
    path('addbus/',views.addbus,name="addbus"),
    path('upbus/<int:rq>/',views.upbus,name="upbus"),
    path('disbus/<int:pq>/',views.disbus,name="disbus"),
    path('dlt/<int:de>/',views.dele,name="del"),
    path('delete/<int:det>/',views.delet,name="dele"),
    path('disp/',views.disp,name="disp"),
    path('pasdata/',views.pasdata,name="pasdata"),
    path('bus/',views.bus,name="bus"),
    path('bookticket/<int:pt>/',views.bookticket,name="bookticket"),
    path('logout/',v.LogoutView.as_view(template_name="ta/logout.html"),name="lgg"),

]