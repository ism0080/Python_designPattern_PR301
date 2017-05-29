with open("table.txt", 'r') as file:
    file_data = file.read()
    # splits on newline
    group = file_data.split('\n')
    line = []
    list_of_dictionaries = []
    i = 0
    for x in group:
        line.extend([group[i].split(', ')])
        list_of_dictionaries.extend([i])
        i += 1
    for empty in list_of_dictionaries:
        list_of_dictionaries[empty] = dict(e.split('=') for e in line[empty])
    for dictionary in list_of_dictionaries:
        print(dictionary)


#
# from datetime import date, datetime
#
# minyear = 1900
# maxyear = date.today().year
#
# mydate = '31-02-2000'
# dateparts = mydate.split('-')
# try:
#     if int(dateparts[2]) > maxyear or int(dateparts[2]) < minyear:
#        raise ValueError("Year out of range")
#     dateobj = date(int(dateparts[2]),int(dateparts[1]),int(dateparts[0]))
# except ValueError as err:
#     print(err)



# def calculate_age(born):
#     today = date.today()
#     print(today)
#     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
#
# if __name__ == '__main__':
#     d = date(1996, 10, 24)
#     print(calculate_age(d))