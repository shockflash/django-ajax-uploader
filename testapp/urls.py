from django.conf.urls.defaults import *
from django.contrib.gis import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.start', name = 'index'),
    url(r'ajax-upload$', 'views.import_uploader', name = "my_ajax_upload"),
)

# serve static files
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
