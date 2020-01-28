# -*- coding: utf-8 -*-
import sys

from os.path import join, isdir

from django.conf.urls import re_path
from django.views.i18n import JavaScriptCatalog

from djangojs.conf import settings
from djangojs.views import UrlsJsonView, ContextJsonView, JsInitView


urlpatterns = [
    re_path(r'^init\.js$', JsInitView.as_view(), name='django_js_init'),
    re_path(r'^urls$', UrlsJsonView.as_view(), name='django_js_urls'),
    re_path(r'^context$', ContextJsonView.as_view(), name='django_js_context'),
    re_path(r'^translation$', JavaScriptCatalog.as_view(), name='js_catalog'),
]
