# coding=utf-8
from oscar.apps.address.forms import AbstractAddressForm
from myapps.order.models import ShippingAddress
from oscar.views.generic import PhoneNumberMixin


class ShippingAddressForm(PhoneNumberMixin, AbstractAddressForm):
    class Meta:
        model = ShippingAddress
        fields = [
            'customer_name', 'line1', 'line4', 'line2', 'detail_address',
            'postcode', 'phone_number', 'notes', 'country'
        ]
        exclude = [
            'title', 'first_name', 'last_name',
            'line3', 'state', 'search_text'
        ]
        labels = {
            "line1": u"省份",
            "line2": u"县区",
        }


from oscar.apps.dashboard.orders.forms import *
