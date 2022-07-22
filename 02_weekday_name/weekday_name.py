from calendar import FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY, calendar
from distutils.command.build_scripts import first_line_re
# print (first_line_re)
# print (WEEK);
def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    s
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    DAY = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
    if day_of_week >= 1 and day_of_week <=7:
        return DAY[day_of_week-1]
    else:
        return "N0ne";
