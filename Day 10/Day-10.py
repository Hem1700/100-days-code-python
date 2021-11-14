# Functions with output

def my_func():
    return 3*2  
final_result = my_func()
print(final_result)




def format_name(first_name, last_name):
    """Take a first and last name and format it to return"""            # Docstrings
    if first_name == " " or last_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = first_name.title()
    formated_l_name = last_name.title()
    return f"{formated_f_name} {formated_l_name}"
formated_name = format_name(input("What is your first name: "), input("What is your last name: "))
print(formated_name)
    


# Day-10-1 Exercise

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(selected_year, selected_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(selected_year) == True and selected_month == 2:
      return 29
  else:
      return month_days[selected_month-1]      


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







