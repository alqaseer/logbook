from django.conf.urls import include, url
from django.contrib import admin
# lower imports to add setting
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #case managment
    url(r'^case_list/$', 'main.views.case_list'),
    url(r'^create_case/$', 'main.views.create_case'),
    url(r'^case_detail/(?P<pk>[0-9]+)/$', 'main.views.case_detail'),
    url(r'^create_update/(?P<pk>[0-9]+)/$', 'main.views.create_update'),
    url(r'^delete1/(?P<pk>[0-9]+)/$', 'main.views.delete1'),
    url(r'^delete2/(?P<pk>[0-9]+)/$', 'main.views.delete2'),
    url(r'^deleteupdate1/(?P<pk>[0-9]+)/$', 'main.views.deleteupdate1'),
    url(r'^deleteupdate2/(?P<pk>[0-9]+)/$', 'main.views.deleteupdate2'),




    #user managment below
    url(r'^signup/$', 'main.views.signup'),
    url(r'^logout/$', 'main.views.logout_view'),
    url(r'^login/$', 'main.views.login_view'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
