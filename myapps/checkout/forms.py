# coding=utf-8
from oscar.apps.address.forms import AbstractAddressForm
from oscar.core.loading import get_model
from myapps.order.models import ShippingAddress
from oscar.views.generic import PhoneNumberMixin

Country = get_model('address', 'Country')


class ShippingAddressForm(PhoneNumberMixin, AbstractAddressForm):
    def __init__(self, *args, **kwargs):
        super(ShippingAddressForm, self).__init__(*args, **kwargs)
        self.adjust_country_field()

    def adjust_country_field(self):
        countries = Country._default_manager.filter(
            is_shipping_country=True, printable_name=u'China')

        # No need to show country dropdown if there is only one option
        if len(countries) == 1:
            self.fields.pop('country', None)
            self.instance.country = countries[0]
        else:
            self.fields['country'].queryset = countries
            self.fields['country'].empty_label = None

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
        },
        help_texts = {
            'phone_number': u'格式："+86 您的电话号码"',
        }



# from oscar.apps.checkout.forms import *
