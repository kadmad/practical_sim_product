from django import forms
from product.models import Product
from product.tasks import populate_products


class ProductInputForm(forms.ModelForm):
    count = forms.IntegerField(required=True)

    class Meta:
        model = Product
        fields = [
            "count",
        ]

    def save(self, force_insert=False, force_update=False):
        count = self.cleaned_data.get("count")
        populate_products.delay(count)
        return count
