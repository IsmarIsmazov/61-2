from django import forms

from product.models import Category, Tag

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


class SearchForm(forms.Form):
    for_test_list = [("1", "test1"), ("2", "test2")]
    choice_list = [("1", "Больше 100"), ("2", "меньше 100")]
    search = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False
    )
    price_choice = forms.ChoiceField(choices=choice_list, required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    for_test = forms.MultipleChoiceField(choices=for_test_list, required=False)
