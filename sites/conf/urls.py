from django.conf.urls import patterns, include, url
from django.contrib import admin

from mobile_products.views import UpdateMobileProductStatusView
from django.views.decorators.csrf import csrf_exempt

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sites.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^update_mobile_product_status/',
        csrf_exempt(UpdateMobileProductStatusView.as_view())),
    url(r'', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    
    
)
