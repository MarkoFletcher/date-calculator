from datetime import datetime, date, timedelta, time

pattern = '%d.%m.%Y'
date_start = date(1994, 6, 18)
date_start_month = date_start.month
date_start_day = date_start.day
#___________________________
date_end = date(2023, 12, 21)
date_end_month = date_end.month
date_end_day = date_end.day

int_year_start_date = date_start.year
int_year_end_date = date_end.year
int_month_start = date_start.month
int_month_end = date_end.month

year_count = 0
month_count = 0

def diffrence(start, end, count):
    while start < end:
        count += 1
        start += 1
    return count

quantity_year = diffrence(int_year_start_date, int_year_end_date, year_count) #разность между дами в годах
quantity_month = diffrence(int_month_start, int_month_end, month_count) #разность между датами в месецах

data_current_year_month = date(int_year_start_date + quantity_year, date_start_month + quantity_month, date_start_day)

def diffrence_year_day(data_current_year_month, date_end):
    return date_end - data_current_year_month

print(f'Результат разности между {datetime.strftime(date_start, pattern)} и {datetime.strftime(date_end, pattern)}: {quantity_year} лет {quantity_month} месяцев {diffrence_year_day(data_current_year_month, date_end).days} дней')


