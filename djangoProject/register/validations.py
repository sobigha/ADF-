"""Validations"""
from datetime import date

from register.models import request_info


class ValidateClass:
    """
    Validation class
    """

    @classmethod
    def age_criteria(cls, gender, date_ofbirth):
        """Calculate the age and check whether criteria matches"""
        gender_check = gender.casefold()
        today_date = date.today()
        age = today_date.year - date_ofbirth.year - \
              ((today_date.month, today_date.day) < \
               (date_ofbirth.month, date_ofbirth.day))
        # print(age)

        var = "Eligible" if gender_check == 'female' and age > 18 or \
                            gender_check == 'male' and age > 21 \
            else "Age is less than expected."
        # logging.info("Age Criteria: %s", self.var)
        return var

    @classmethod
    def pan_criteria(cls, pannumber):
        """Check if request has received or not in last 5 days"""

        myresult = ""
        for p_val in request_info.objects.raw('SELECT id,request_date FROM  \
                                      register_request_info WHERE pan_number = %s', [pannumber]):
            myresult = p_val.request_date
        print(myresult)
        var = None if myresult is None else myresult
        print(var)
        # logging.info("Pan Criteria: %s", var)
        return var

    @classmethod
    def check_date(cls, myresult):
        """Check if Recently request received in last 5 days"""
        result_r = str(myresult)
        req_date = result_r.replace("-", " ").split(" ")
        # print("c",req_date)
        year_n = int(req_date[0])
        month_n = int(req_date[1])
        date_n = int(req_date[2])
        date_n = date(year_n, month_n, date_n)
        today_n = date.today()
        age = (today_n - date_n).days
        var = "Eligible" if age > 5 else \
            "Recently request received in last 5 days."
        # logging.info("Check Date: %s", var)
        return var

    @classmethod
    def nationality_criteria(cls, nation):
        """Check the nationality criteria"""
        nationality_test = nation.casefold()
        test_list = ['indian', 'american']
        var = "Eligible" if nationality_test in test_list \
            else "Nationality does not match"
        # logging.info("Nationality Criteria: %s", var)
        return var

    @classmethod
    def state_criteria(cls, state_detail):
        """Check the state criteria"""
        state_test = state_detail.casefold()
        test_list = ['andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', \
                     'chhattisgarh', 'karnataka', 'madhya pradesh', \
                     'odisha', 'tamil nadu', 'telangana', 'west bengal']

        var = "Eligible" if state_test in test_list else "State does not match"
        # logging.info("State Criteria: %s", var)
        return var

    @classmethod
    def salary_criteria(cls, salary):
        """Check the salary criteria"""
        var = "Eligible" if 10000 <= salary <= 90000 else "Salary is not within the range"
        # logging.info("Salary Criteria: %s", var)
        return var
