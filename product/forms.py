from django import forms

spisok_bad_words = ["ismar", "казино"]


class CreateProductForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()
    price = forms.IntegerField()

    def clean(self):
        data = self.cleaned_data
        name = data.get("name")
        if name in spisok_bad_words:
            raise forms.ValidationError("Это слово запрещено")
        return data
