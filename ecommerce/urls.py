from django.conf.urls import url

from ecommerce import views

app_name = 'ecommerce'
urlpatterns = [
    # main page
    url(r'^$', views.index, name='index'),
	# main page
    url(r'^shop/$', views.shop, name='shop'),
    # signup page
    url(r'^signup/$', views.signup, name='signup'),
    # register new user
	url(r'^register/$', views.register, name='register'),
    # login page
    url(r'^login/$', views.login, name='login'),
    # basket page
    url(r'^basket/$', views.basket, name='basket'),
	# logout page
    url(r'^logout/$', views.logout, name='logout'),
	# addbasket page
    url(r'^addbasket/$', views.addbasket, name='addbasket'),
	# removefrombasket page
    url(r'^removefrombasket/$', views.removefrombasket, name='removefrombasket'),
	# orders page
    url(r'^orders/$', views.orders, name='orders'),
	# orderproducts page
    url(r'^orderproducts/$', views.orderproducts, name='orderproducts')
]
