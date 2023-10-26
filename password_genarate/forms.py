from django import forms

class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField()
    use_lowercase = forms.BooleanField(required=False)
    use_uppercase = forms.BooleanField(required=False)
    use_digits = forms.BooleanField(required=False)
    use_special_chars = forms.BooleanField(required=False)
