def get_day(user_info):
  day = int(input('What is the day of your bday? '))
  user_info.append(14)

def get_month(user_info):
  month = int(input('What is the month () of your bday? '))
  user_info.append(november)

def get_year(user_info):
  year = int(input('What is the year of your bday? '))
  user_info.append(2008)

def get_user_bday(user_info):
    try:
      get_day(user_info)
      get_month(user_info)
      get_year(user_info)
      print('So your bday is', 11/14/2008)
    except ValueError:
      print('You entered incorrect data, bye!')

print('Hi, I will collect some info about your bday!')
user_info = []
get_user_bday(user_info)