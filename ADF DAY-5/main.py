"""Program to get the user details"""
import re
import json
import logging
from datetime import date
from db_file import mycursor,mydb

logging.basicConfig(
    filename="log_file.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
    force=True
)


class Details:
    """
    Class to validate
    user details
    """
    def __init__(self):
        self.age = None
        self.test_list = None
        self.var = None


    def age_criteria(self,gender,date_ofbirth):
        """Calculate the age and check whether criteria matches"""
        gender_check = gender.casefold()
        today_date = date.today()
        self.age = today_date.year - date_ofbirth.year - ((today_date.month, today_date.day) < \
                                                (date_ofbirth.month, date_ofbirth.day))
        # print(age)

        self.var = "Eligible" if gender_check == 'female' and self.age > 18 or \
               gender_check == 'male' and self.age > 21 else "Age is less than expected."
        logging.info("Age Criteria: %s", self.var)
        return self.var


    def pan_criteria(self,pannumber):
        """Check if request has received or not in last 5 days"""

        sql_query = "SELECT request_date from request_info WHERE pan_number = %s"
        store = (pannumber,)
        mycursor.execute(sql_query, store)
        myresult = mycursor.fetchone()

        self.var = myresult if myresult is not None else "Not Elgibile"
        logging.info("Pan Criteria: %s", self.var)
        return self.var


    def check_date(self,myresult,pannumber):
        """Check if Recently request received in last 5 days"""
        request = ""
        for i in myresult:
            request += str(i)

        req_date = re.sub("-", " ", request).split(" ")
        year_n = int(req_date[0])
        month_n = int(req_date[1])
        date_n = int(req_date[2])
        date_n = date(year_n, month_n, date_n)
        today_n = date.today()
        age = (today_n - date_n).days
        self.var = "Eligible" if age > 5 else \
              "Recently request received in last 5 days."
        if age > 5: \
                mycursor.execute("UPDATE request_info SET request_date = %s \
                WHERE pan_number = %s",(today_n,pannumber))
        logging.info("Check Date: %s", self.var)
        return self.var


    def nationality_criteria(self,nation):
        """Check the nationality criteria"""
        nationality_test = nation.casefold()
        self.test_list = ['indian', 'american']
        self.var = "Eligible" if nationality_test in self.test_list \
                   else "Nationality does not match"
        logging.info("Nationality Criteria: %s", self.var)
        return self.var


    def state_criteria(self,state_detail):
        """Check the state criteria"""
        state_test = state_detail.casefold()
        self.test_list = ['andhra pradesh', 'arunachal pradesh', 'assam', 'bihar', \
                     'chhattisgarh', 'karnataka', 'madhya pradesh', \
                     'odisha', 'tamil nadu', 'telangana', 'west bengal']

        self.var = "Eligible" if state_test in self.test_list else "State does not match"
        logging.info("State Criteria: %s", self.var)
        return self.var


    def salary_criteria(self,salary):
        """Check the salary criteria"""
        self.var = "Eligible" if 10000 <= salary <= 90000 else "Salary is not within the range"
        logging.info("Salary Criteria: %s", self.var)
        return self.var


first_name = input("Enter First Name : ")
middle_name = input("Enter Middle Name : ")
last_name = input("Enter Last Name : ")
date_of_birth = input("Enter Date Of Birth in YYYY-MM-DD : ")
gender_detail = input("Enter Gender : ")
nationality = input("Enter Nationality : ")
current_city = input("Enter Currrent City : ")
state = input("Enter State : ")
pin_code = int(input("Enter Pincode : "))
qualification = input("Enter Qualification : ")
salary_details = int(input("Enter Salary Details : "))
pan_number = input("Enter PAN Number : ")



today = date.today()
current_date = today.strftime("%Y-%m-%d")
# print(current_date)

SQL = "SELECT pan_number FROM request_info WHERE pan_number = %s"
value = (pan_number,)
mycursor.execute(SQL, value)
result = mycursor.fetchall()
# print(result)
# print(mycursor.rowcount)
result = mycursor.rowcount
X = 0 if result == 0 else 1

if X == 1: \
        SQL = "SELECT id_num FROM request_info WHERE pan_number = %s"
if X == 1: \
        value = (pan_number,)
if X == 1: \
        mycursor.execute(SQL, value)
if X == 1: \
        num_id = mycursor.fetchone()
if X == 1: \
        num_id = num_id[0]
# print(id)

SQL_FORM = "INSERT INTO request_info(first_name,middle_name, \
            last_name,date_ofbirth,gender,nationality,current_city, \
            state,pin_code,qualification, salary,pan_number,request_date) \
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" if X == 0 else \
           "UPDATE request_info SET first_name = %s,middle_name = %s,\
            last_name = %s,date_ofbirth = %s, gender = %s,nationality = %s, \
            current_city = %s,state = %s,pin_code = %s,qualification = %s, \
            salary = %s,pan_number = %s WHERE id_num = %s"

tuple_value = (first_name, middle_name, last_name, date_of_birth, gender_detail,\
               nationality, current_city,state, pin_code, qualification, salary_details, \
               pan_number, current_date) if X == 0 else (first_name, middle_name, last_name, \
              date_of_birth, gender_detail, nationality, current_city, \
              state, pin_code, qualification, salary_details, pan_number,  num_id)

mycursor.execute(SQL_FORM, tuple_value)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
logging.info("Values Inserted")

obj = Details()
dob = date_of_birth.replace('-', ' ').split(' ')
year = int(dob[0])
month = int(dob[1])
date1 = int(dob[2])

RESPONSE_RESULT = "Eligible"
SAMPLE_STR = ""

if RESPONSE_RESULT == "Eligible": \
        RESPONSE_RESULT = obj.age_criteria(gender_detail,date(year, month, date1))
if RESPONSE_RESULT == "Eligible": \
         SAMPLE_STR= obj.pan_criteria(pan_number)
if SAMPLE_STR != "Not Eligible": \
        RESPONSE_RESULT = obj.check_date(SAMPLE_STR,pan_number)
if RESPONSE_RESULT == "Eligible": \
        RESPONSE_RESULT = obj.nationality_criteria(nationality)
if RESPONSE_RESULT == "Eligible": \
        RESPONSE_RESULT = obj.state_criteria(state)
if RESPONSE_RESULT == "Eligible": \
        RESPONSE_RESULT = obj.salary_criteria(salary_details)

SQL = "SELECT id_num FROM request_info WHERE pan_number = %s"
value = (pan_number,)
mycursor.execute(SQL, value)
id_fetch = mycursor.fetchone()
id_fetch = id_fetch[0]

ID_NUM = "'Request_id':" + str(id_fetch)
RESULT_SUCCESS = ",'Response':'Success'"
RESULT_FAILURE = ",'Response':'Failed','Reason':" + "\'" + RESPONSE_RESULT + "\'"

RESULT = RESULT_SUCCESS if RESPONSE_RESULT == "Eligible" else RESULT_FAILURE
Dict = dict({ID_NUM: RESULT})

Dict = json.dumps(Dict)
print(Dict)
logging.info("Converted to dumps")

SQL_FORM = "INSERT INTO response_info(request_id,response_message) VALUES (%s,%s)"
tuple_value = (id_fetch, Dict)
# print(id)
mycursor.execute(SQL_FORM, tuple_value)
mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

retrieve = json.loads(Dict)
logging.info("Converted to loads")
print(str(retrieve))
