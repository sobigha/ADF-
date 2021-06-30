"""Receives Request and sends response"""

import logging
import json
from datetime import date
# pylint: disable=R0915,E0401
from django.http import HttpResponse
from django.shortcuts import render
from register.forms import Formclass
from register.models import request_info, response_info
from register.validations import ValidateClass


def index(request):
    """Render to template"""
    form = Formclass()
    context = {
        "registerform": form
    }
    return render(request, 'register.html', context)


# pylint: disable=R0912
def user(request):
    """Validate the user input and store in database"""
    if request.method == "POST":
        form = Formclass(request.POST)
        flag = 0

        if form.is_valid():
            print("0")
            x_val = 0
            pan = form.cleaned_data.get('pan_number')
            for p_val in request_info.objects.raw(
                    'SELECT id,pan_number,request_date FROM register_request_info \
                     WHERE pan_number = %s', [pan]):
                print("1", p_val.pan_number)
                print("2", p_val.id)
                x_val = p_val.id
            if x_val == 0:
                flag = 1
            if x_val != 0:
                print("in")
                print("5", flag)
                request_info.objects.filter(id=x_val).update \
                    (first_name=form.cleaned_data.get('first_name'), \
                     middle_name=form.cleaned_data.get('middle_name'), \
                     last_name=form.cleaned_data.get('last_name'), \
                     date_ofbirth=form.cleaned_data.get('date_ofbirth'), \
                     gender=form.cleaned_data.get('gender'), \
                     nationality=form.cleaned_data.get('nationality'), \
                     city=form.cleaned_data.get('city'), \
                     state=form.cleaned_data.get('state'), \
                     pin_code=form.cleaned_data.get('pin_code'), \
                     qualification=form.cleaned_data.get('qualification'), \
                     salary=form.cleaned_data.get('salary'), \
                     pan_number=form.cleaned_data.get('pan_number') \
                     )

        if flag == 1:
            print("4")
            if request.method == "POST":
                form = Formclass(request.POST)
                print("4")
                form.save()

        response_result = "Eligible"
        sample_str = ""
        sample = ""

        obj = ValidateClass
        gender = form.cleaned_data.get('gender')
        print(gender)

        date_ofbirth = str(form.cleaned_data.get('date_ofbirth'))
        print(date_ofbirth)
        dob = date_ofbirth.replace('-', ' ').split(' ')
        year = int(dob[0])
        month = int(dob[1])
        date1 = int(dob[2])

        state = form.cleaned_data.get('state')
        print(state)

        nationality = form.cleaned_data.get('nationality')
        print(nationality)

        pan = form.cleaned_data.get('pan_number')
        print(pan)

        salary = form.cleaned_data.get('salary')
        print(salary)

        if response_result == "Eligible": \
                response_result = obj.age_criteria(gender, date(year, month, date1))
        print(response_result)

        if response_result == "Eligible": \
                sample_str = obj.pan_criteria(pan)
        print("o", sample_str)

        if sample_str is not None and sample_str != "": \
                sample = "Eligible"
        if sample == "Eligible": \
                response_result = obj.check_date(sample_str)
        print(response_result)

        y_val = 0
        for p_val in request_info.objects.raw(
                'SELECT id,pan_number FROM register_request_info WHERE pan_number = %s', [pan]):
            y_val = p_val.id
        request_info.objects.filter(id=y_val).update(request_date=date.today())

        if response_result == "Eligible": \
                response_result = obj.nationality_criteria(nationality)
        print(response_result)

        if response_result == "Eligible": \
                response_result = obj.state_criteria(state)
        print(response_result)

        if response_result == "Eligible": \
                response_result = obj.salary_criteria(salary)
        print(response_result)

        id_fetch = y_val
        id_num = "'Request_id':" + str(id_fetch)
        result_success = ",'Response':'Success'"
        result_failure = ",'Response':'Failed','Reason':" + "\'" + response_result + "\'"

        result = result_success if response_result == "Eligible" else result_failure
        dict_id = dict({id_num: result})
        data = response_table(dict_id, y_val)
        return HttpResponse(data)


def response_table(dict_id, req_id):
    """Store the response in response_info table nn  """
    dict_id = json.dumps(dict_id)
    print(dict_id)
    logging.info("Converted to dumps")

    form_res = response_info(request_id_id=req_id, response_message=dict_id)
    form_res.save()

    retrieve = json.loads(dict_id)
    logging.info("Converted to loads")
    print(str(retrieve))
    return str(retrieve)
