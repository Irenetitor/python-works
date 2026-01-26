from datetime import datetime, date, time, timedelta


# 1. Create a variable with the current date and time.

current_datetime = datetime.now()
print(current_datetime)

# 2. Print only the year, month, and day of the current date.

current_date = date.today()
print(current_date)

# 3. Create a specific date: December 25, 2025 and display it.

specific_date = date(2025, 12, 25)
print(specific_date)

# 4. Display only the hours, minutes, and seconds of a time object.

time_objct = time(12, 37, 46)
print(time_objct)

# 5. Calculate how many days are left until January 1 of the following year.

new_year = date(2026, 1, 1)
print(new_year - current_date)

# 6. Create a function that receives a date and returns its timestamp.

def get_date():
    date_str = input("Introduce date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.timestamp()

print(get_date())


# 7. Add 30 days to the current date using timedelta.

sum_days = current_date + timedelta(days=30)
print(sum_days)

# 8. Create a date and add 1 month (tip: do it by adding 30 days as a simplification).

ini_date = datetime(2023, 4, 17)
after_month = ini_date + timedelta(days=30)
print(after_month)

# 9. Compare two dates and display which one is earlier.

d1 = date(2025, 7, 23)
d2 = date(2025, 3, 1)

if d1 < d2:
    print(f"{d1} is before {d2}")
else:
    print(f"{d2} is before {d1}")


# 10. Create a list with several dates and sort them chronologically.

list_dates = [(2023, 3, 24), (2024, 6, 27), (2022, 5, 14), (2022, 12, 21)]

dates = [date(y, m, d) for y, m, d in list_dates]
ordered_dates = sorted(dates)

print(ordered_dates)


current_time = time(21,6,0)
print(current_time.hour)