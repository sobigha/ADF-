"""Form class"""

from django import forms
# from django.forms import ModelForm

#from register.models import request_info, response_info


# pylint: disable = R0903
class Formclass(forms.Form):
    """
    form's field and labels
    """

    class Meta:
        """
        Fields and labels
        """
       # model = request_info
        fields = ["first_name", "middle_name", "last_name", "date_ofbirth",
                  "gender", "nationality", "city", "state", "pin_code",
                  "qualification", "salary", "pan_number"]
        labels = {'first_name': "FIRST NAME", 'middle_name': "MIDDLE NAME",
                  'last_name': "LAST NAME", 'date_ofbirth': "DATE OF BIRTH", 'gender': "GENDER",
                  'nationality': "NATIONALITY", 'city': "CITY", 'state': "STATE",
                  'pin_code': "PINCODE", 'qualification': "QUALIFICATION", \
                  'salary': "SALARY", 'pan_number': "PAN NUMBER"}


# class validate(ModelForm):
#     """
#     Response info
#     """
#
#     class Meta:
#         """
#         Response info
#         """
#         model = response_info()
#         fields = ["request_id", "response_message"]
