from oscar.apps.checkout.views import ShippingAddressView as CoreShippingAddressView


class ShippingAddressView(CoreShippingAddressView):
    from myapps.checkout.forms import ShippingAddressForm
    form_class = ShippingAddressForm



