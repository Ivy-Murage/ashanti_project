# year_code
def year_code(year):
    yy = year % 100
    return (yy + (yy // 4)) % 7


dict_month = {'January': 0,
              'February': 3,
              'March': 3,
              'April': 6,
              'May': 1,
              'June': 4,
              'July': 6,
              'August': 2,
              'September': 5,
              'October': 0,
              'November': 3,
              'December': 5}


def centrury_code(year):
    global century
    century = year // 100
    return century





def leap_year(year):
    if year % 4 == 0 or year % 400 == 0:
        return 1
    elif year % 100 == 0:
        return 0
    else:
        return 0


dict_century = {17: 4,
                18: 2,
                19: 0,
                20: 6,
                21: 4,
                22: 2,
                23: 0}


dict_day = {0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday"}

my_ashanti = {"Sunday": {"female": "Akosua","male": "Kwasi"},
              "Monday": {"female": "Adjou", "male": "Kodjo"},
              "Wednesday": {"female": "Abenaa", "male": "Kwabena"},
              "Thursday": {"female": "Akua", "male": "Kwaku"},
              "Friday": {"female": "Afia", "male": "Kofia"},
              "Saturday": {"female": "Amma", "male": "Kwame"}}



def name_input():
    year = int(input("Enter the year you were born: "))
    month = input("Enter the month you were born: ")
    date = int(input("Enter the date of the month you were born: "))
    gender = input("Enter your gender: ")
    year_1 = year_code(year)
    centrury_code(year)
    leap = leap_year(year)
    month = dict_month[month]
    temp = dict_century[century]
    day_var = day(year_1, month, temp, date, leap)
    var = (dict_day[day_var])
    ashanti_name = my_ashanti[var]
    if gender == "female":
        m = ashanti_name["female"]

    else:
       m =  ashanti_name["male"]
    print("If you were an ashanti person your name would have been {}".format(m))

def day(year_1, month, century, date_number, leap):
    return (year_1 + month + century + date_number - leap) % 7







name_input()

