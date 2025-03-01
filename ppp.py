from datetime import datetime
from cs1033_evaluator import evaluate_L6_E2

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January 
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January 
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################


# Your code should be included here. 
file_name=input()
file=list(open('file_name','r'))
print(file)
file.close()
# You may use the days_to_birthday(date) function in your solution.


################################################################################
# Please do not edit anything below this line.
evaluate_L6_E2()

##################### End of the programme #####################################
