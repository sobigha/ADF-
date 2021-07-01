"""Models python file"""

from django.db import models


class request_info(models.Model):
    """
    Request info table
    """
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_ofbirth = models.DateField()
    gender = models.CharField(max_length=8)
    nationality = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    qualification = models.CharField(max_length=20)
    salary = models.IntegerField()
    pan_number = models.CharField(max_length=20)
    request_date = models.DateField(null=True, blank=True)


class response_info(models.Model):
    """
    Response info table
    """
    request_id = models.ForeignKey(request_info, on_delete=models.CASCADE)
    response_message = models.CharField(max_length=150)
