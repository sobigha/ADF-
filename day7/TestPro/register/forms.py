"""Forms"""
from django import forms


class FormClass(forms.Form):
    """
    Form class
    """
    first_name = forms.CharField(max_length=50)
    middle_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    date_ofbirth = forms.DateField()
    gender = forms.CharField(max_length=8)
    nationality = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)
    pin_code = forms.IntegerField()
    qualification = forms.CharField(max_length=20)
    salary = forms.IntegerField()
    pan_number = forms.CharField(max_length=20)
# request_date = forms.DateField(null=True, blank=True)
