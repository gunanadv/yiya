from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register_view, name='register_view'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^selfi/$', views.selfi_view, name='selfi_view'),
    url(r'^article/(?P<id>.*)$', views.article_view, name='article_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^application/(?P<id>.*)$', views.application_view, name='application_view'),
    url(r'^admin_console/$', views.admin_console, name='admin_console'),
    url(r'^consultation-submit/$', views.consultation_submit, name='consultation_submit'),
    url(r'^forget-password-submit/$', views.forget_password_submit, name='forget_password_submit'),
    url(r'^new-password-submit/$', views.new_password_submit, name='new_password_submit'),
    url(r'^admin_application/(?P<id>.*)$', views.admin_application_view, name='admin_application_view'),
    url(r'^admin_student/(?P<id>.*)$', views.admin_student_view, name='admin_student_view'),
    url(r'^application-create-submit/$', views.application_create_submit, name='consultation_submit'),
    url(r'^articles/$', views.articles_view, name='articles_view'),

    

]

