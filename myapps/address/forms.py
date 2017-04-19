# coding=utf-8
from oscar.apps.address.forms import AbstractAddressForm
from myapps.address.models import UserAddress
from oscar.views.generic import PhoneNumberMixin


class UserAddressForm(PhoneNumberMixin, AbstractAddressForm):
    def __init__(self, user, *args, **kwargs):
        super(UserAddressForm, self).__init__(*args, **kwargs)
        self.instance.user = user

    class Meta:
        model = UserAddress
        fields = [
            'customer_name', 'line1', 'line4', 'line2', 'detail_address',
            'postcode', 'country'
        ]
        exclude = [
            'title', 'first_name', 'last_name',
            'line3', 'state', 'search_text'
        ]
        labels = {
            "line1": u"省份",
            "line2": u"县区",
        }

from oscar.apps.address.forms import *
