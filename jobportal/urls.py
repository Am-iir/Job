from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from jobs.views import home,about,post_job,job_list,user_list ,job_detail ,job_update , job_delete,user_posted

from accounts.views import login_view, logout_view , signup_view 


urlpatterns = [
    # Examples:
    # url(r'^$', 'jobportal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', about, name='about'),
    url(r'^$', home, name='home'),
    url(r'^post/$', post_job, name='post_job'),
    url(r'^joblist/$', job_list, name='job_list'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^login/$', login_view, name='login'),
    url(r'^signup/$', signup_view, name='signup'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^view/user/(?P<username>\w+)/$', user_list, name='user_list'),
    url(r'^view/user/$',user_list, name='user_list'),
    url(r'^(?P<id>\d+)/detail/$', job_detail,name='detail'),
    url(r'^(?P<id>\d+)/userposted/$', user_posted,name='userpost'),
    url(r'^(?P<id>\d+)/update/$', job_update,name='update'),
    url(r'^(?P<id>\d+)/delete/$', job_delete,name='delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
