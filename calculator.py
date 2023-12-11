from datetime import datetime, date
from Tkinter_window import receive_text

# Входные данные:

pattern = '%d.%m.%Y'


print(receive_text(), 'wqwrqw')


date_start = date(2000, 9, 13)
date_start_month = int(date_start.month)
date_start_day = int(date_start.day)

date_end = date(2023, 6, 19)
date_end_month = int(date_end.month)
date_end_day = int(date_end.day)

int_year_start_date = int(date_start.year)
int_year_end_date = int(date_end.year)

int_month_start = int(date_start.month)
int_month_end = int(date_end.month)


def word_conversion(digit: int, word: list[str]) -> str:
    if digit % 10 == 1 and digit % 100 != 11:
        return f'{digit} {word[0]}'
    elif digit % 10 in (2, 3, 4) and not digit % 100 in (12, 13, 14):
        return f'{digit} {word[1]}'
    else:
        return f'{digit} {word[2]}'


if date_start_day <= date_end_day and date_start_month < date_end_month:
    quantity_year = int_year_end_date - int_year_start_date
    quantity_month = date_end_month - date_start_month
    days_count = date_end_day - date_start_day

elif date_start_day > date_end_day and date_start_month < date_end_month:
    quantity_year = int_year_end_date - int_year_start_date
    quantity_month = date_end_month - date_start_month - 1  # разность между датами в месецах
    data_current_year_month = date(int_year_start_date + quantity_year, date_start_month + quantity_month, date_start_day)  # текущая дата с месяцвми и годами
    days_count = (date_end - data_current_year_month).days


elif date_start_day <= date_end_day and date_start_month > date_end_month:
    quantity_year = int_year_end_date - int_year_start_date - 1  # разность между дами в годах
    quantity_month = 12 - date_start_month + date_end_month
    days_count = date_end_day - date_start_day

elif date_start_day > date_end_day and date_start_month > date_end_month:
    quantity_year = int_year_end_date - int_year_start_date - 1  # разность между дами в годах
    quantity_month = 12 - date_start_month + date_end_month - 1
    data_current_year_month = date(int_year_end_date, date_end_month - 1, date_start_day)
    days_count = date_end - data_current_year_month


quantity_year_conversion = word_conversion(quantity_year, word=['год', 'года', 'лет'])
quantity_month_conversion = word_conversion(quantity_month, word=['месяц', 'месяца', 'месяцев'])
days_count_conversion = word_conversion(days_count, word=['день', 'дня', 'дней'])

print(f'Результат разности между {datetime.strftime(date_start, pattern)} и {datetime.strftime(date_end, pattern)}: '
      f'{quantity_year_conversion} {quantity_month_conversion} {days_count_conversion}')




