from django.shortcuts import render_to_response
from django.template import RequestContext
from ajaxuploader.views import AjaxFileUploader
from ajaxuploader.backends.local import LocalUploadBackend
from django.middleware.csrf import get_token

def start(request):
    csrf_token = get_token(request)
    return render_to_response('django-ajax-uploader/sample.html', {}, context_instance = RequestContext(request))


class MyAjaxFileUploader(AjaxFileUploader):

    def __call__(self, request):
        response = super(MyAjaxFileUploader, self).__call__(request)

        print "Do something with the data here", self.filename

        return response



import_uploader = MyAjaxFileUploader(backend = LocalUploadBackend)
