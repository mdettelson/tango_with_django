from django import forms
from Rango.models import Page, Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(),
                               initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(),
                               initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(),
                           required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(),
                               initial=0)


    class Meta:
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # We can either exclude the category field from the form,
        exclude = ('category',)
        # or specify the fields to include
        # fields = ('title', 'url', 'views')