# This maps a month number to its abbreviation,
# and abbreviation to its number.
# Mapping is one-way, so they have to be defined both ways,
# since I will be using the numbers for looping.
months = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "may",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "oct",
    11: "nov",
    12: "dec",
    "jan": 1,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12
}

# Maps a month abbreviation to the number of days that month (typically) has.
days_in_month = {
    "jan": 31,
    "feb": 28,
    "mar": 31,
    "apr": 30,
    "may": 31,
    "jun": 30,
    "jul": 31,
    "aug": 31,
    "sep": 30,
    "oct": 31,
    "nov": 30,
    "dec": 31
}


def main():
    print(days_between("June 19 1922", "Jun 19 1922"))
    print(days_between("June 19 1922", "Jun 21 1922"))
    print(days_between("June 19 1922", "July 14 1922"))
    print(days_between("June 19 1922", "April 5 2014"))


def days_between(date_start, date_end):
    # Split the input into an array of three strings
    date_start = date_start.split()
    date_end = date_end.split()
    # Month to first three characters in lowercase
    month_start = date_start[0][:3].lower()
    month_end = date_end[0][:3].lower()
    # Day to number
    day_start = int(date_start[1])
    day_end = int(date_end[1])
    # Year to number
    year_start = int(date_start[2])
    year_end = int(date_end[2])

    # Probably an unnecessary check, but don't break my code.
    if (month_start == "feb" and day_start == 29 and not is_leap_year(year_start)) or (
            (not (month_start == "feb" and day_start == 29)) and days_in_month[month_start] < day_start):
        raise Exception(" ".join(date_start) + " is not a real date")
    if (month_end == "feb" and day_end == 29 and not is_leap_year(year_end)) or (
            (not (month_end == "feb" and day_end == 29)) and days_in_month[month_start] < day_end):
        raise Exception(" ".join(date_end) + " is not a real date")

    # If both dates are in the same year
    if year_start == year_end:
        day_count = day_of_the_year(month_end, day_end, year_end) - day_of_the_year(month_start, day_start, year_start)
    # If dates are in different years
    else:
        # Add the number of days remaining in the year
        day_count = 365 - day_of_the_year(month_start, day_start, year_start)
        if is_leap_year(year_start):
            day_count += 1
        # For each year between the two, add the number of days in the year.
        # I use a loop instead of multiplication because it's easier to just check if each is a leap year.
        # Range excludes the upper bound, so this doesn't add the number of days in the last year.
        for year in range(year_start + 1, year_end):
            day_count += 365
            if is_leap_year(year):
                day_count += 1
        # For the last year, just add the day-of-the-year (number) that the date falls on.
        day_count += day_of_the_year(month_end, day_end, year_end)

    return day_count


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def day_of_the_year(month, day, year):
    days = 0
    # For the first n - 1 months,
    # add the amount of days in the month.
    # I use m so I don't overwrite month (the string that's passed).
    for m in range(1, months[month]):
        days += days_in_month[months[m]]
    # For the month of the given date,
    # add the day of the month
    days += day
    # And account for leap years
    if is_leap_year(year) and months[month] > 2:
        days += 1
    return days


# Entry point for the program
if __name__ == "__main__":
    main()
