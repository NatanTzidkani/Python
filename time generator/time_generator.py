def gen_secs():
    sc = 0
    while True:
        yield sc
        sc = (sc + 1) % 60


def gen_minutes():
    mn = 0
    while True:
        yield mn
        mn = (mn + 1) % 60


def gen_hours():
    hr = 0
    while True:
        yield hr
        hr = (hr + 1) % 24


def gen_time():
    sec = gen_secs()
    mn = gen_minutes()
    hour = gen_hours()
    current_sec = next(sec)
    current_min = next(mn)
    current_hr = next(hour)
    flag_min = False
    flag_sec = False
    while True:
        yield "%02d:%02d:%02d" % (current_hr, current_min, current_sec)
        if current_sec == 59:
            flag_sec = True
        if current_min == 59:
            flag_min = True
        current_sec = next(sec)
        if current_sec == 0 and flag_sec:
            current_min = next(mn)
            flag_sec = False
        elif current_min == 00 and flag_min:
            current_hr = next(hour)
            flag_min = False


def gen_years(start=2019):
    start = start
    while True:
        yield start
        start += 1


def gen_months():
    sc = 0
    while True:
        yield sc + 1
        sc = (sc + 1) % 12


def gen_days(month, leap_year=True):
    not_leap_month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while True:
        if leap_year:
            yield leap_month_days[month - 1]
            month = (month + 1) % 12
        else:
            yield not_leap_month_days[month - 1]
            month = (month + 1) % 12


# let's do it easier, if next gen_time(external_gen_day) == 000000 then next day
# every year need to check if the year is leap or not


def gen_date():
    yr = gen_years()
    month = gen_months()
    clock = gen_time()

    current_day = 1
    current_month = next(month)
    current_year = next(yr)
    days_in_month = gen_days(current_month, (current_year % 400 == 0 or
                                             (current_year % 4 == 0 and current_year % 100 != 0)))
    days = next(days_in_month)

    for t in clock:
        yield "%02d/%02d/%04d" % (current_day, current_month, current_year) + " " + t
        if t == "23:59:59":
            current_day += 1
            if current_day > days:
                current_day = 1
                if current_month == 12:
                    current_year = next(yr)
                    days_in_month = gen_days(current_month, (current_year % 400 == 0 or
                                                             (current_year % 4 == 0 and current_year % 100 != 0)))
                current_month = next(month)
                days = next(days_in_month)



    # current_year = next(yr)
    # current_month = next(mon)
    # month_days = gen_days(current_month, (current_year % 400 == 0 or (current_year % 4 == 0 and current_year % 100 != 0)))
    #
    # current_days = next(month_days)
    # last_day_at_month = current_days - 1
    # current_day = 1
    #
    # current_time = next(clock)

    # flags to check the last periods:

    # flag_clock = False  # checks if time is 00:00:00
    # flag_day = False  # checks if the month is finished
    # flag_year = False  # checks if the year is finished
    #
    #
    # while True:
    #     if current_day == last_day_at_month - 1:
    #         flag_month = True  # then current_days = next(month_days)
    #     if current_time == "23:59:59":
    #         flag_clock = True
    #     if current_month == 12 and flag_clock and flag_month:
    #         flag_year = True
    #
    #     yield "%02d/%02d/%04d" % (current_day, current_month, current_year) + " " + current_time
    #
    #     current_time = next(clock)
    #
    #     if current_time == "00:00:00" and flag_clock:
    #         current_day += 1
    #         flag_clock = False
    #         if (current_day == last_day_at_month + 1) and flag_month:
    #             current_month = next(mon)
    #             month_days = gen_days(current_month, (current_year % 400 == 0 or (current_year % 4 == 0 and current_year % 100 != 0)))
    #             current_days = next(month_days)
    #             last_day_at_month = current_days - 1
    #             current_day = 1
    #             flag_month = False
    #             if flag_year and current_time == "00:00:00" and flag_clock:
    #                 current_year = next(yr)



calender = gen_date()
for i in range(1000):
    print(next(calender))
