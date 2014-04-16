from django.http.response import HttpResponse
from django.views.generic.base import View

from mobile_products.models import MobileProduct


class UpdateMobileProductStatusView(View):

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        status = request.POST['status']
        MobileProduct.objects.filter(id=id).update(status=status)
        response_kwargs = {'status':200,
                           'content_type':'application/json'}
        return HttpResponse({}, **response_kwargs)
