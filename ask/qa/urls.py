from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import qa
from qa import views
urlpatterns = [
	url(r'^', qa.views.test),
	url(r'^login/', qa.views.test),
	url(r'^signup/', qa.views.test),
	url(r'^question/', qa.views.test),
	url(r'^ask/', qa.views.test),
	url(r'^popular/', qa.views.test),
	url(r'^new/', qa.views.test),
]
