from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import qa
from qa import views
urlpatterns = [
	url(r'^$', qa.views.home),
	#url(r'^login/$', login.site.urls),/(?P<page>\d+)
	url(r'^signup/$', qa.views.test),
	url(r'^question/(?P<id>\d+)/$', qa.views.question),
	url(r'^ask/\D*$', qa.views.test),
	url(r'^popular/$', qa.views.popular),
	url(r'^new/$', qa.views.test),
]
