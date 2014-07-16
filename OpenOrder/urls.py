from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import *
from userena import views as userena_views
from userena.views import *
import os

admin.autodiscover()

site_dir = os.path.dirname(settings.PROJECT_DIR)
doc_root = os.path.join(os.path.dirname(site_dir), 'docs/build/html')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OpenOrder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',userena_views.signin,name='userena_signin'),
    url(r'^admin/doc/',        include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blogango.urls' ) ,name= 'blog'),
    url(r'^accounts/', include('userena.urls')),
    url(r'^message/', include('django_messages.urls')),
    url(r'^polls/', include('Order.urls' , namespace="polls")),
    url(r'^contact/', include('contact_form.urls' , namespace="contact")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
