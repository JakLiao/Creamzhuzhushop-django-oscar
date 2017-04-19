from oscar.apps.dashboard.orders.views import ShippingAddressUpdateView as CoreShippingAddressUpdateView


class ShippingAddressUpdateView(CoreShippingAddressUpdateView):
    from myapps.dashboard.orders.forms import ShippingAddressForm
    form_class = ShippingAddressForm