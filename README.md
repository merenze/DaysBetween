# Days Between

Calculates the number of days between two dates.

## Usage
The application takes no arguments.

When the application prompts for input dates,
provide a date with a month-day-year format,
using the full name or abbreviation of a month
and a four-digit year.

Months are case-insensitive, and only the first
three characters of the month are used.

Do not use punctuation or special characters.

Valid date formats include:
* August 1 1992
* Jan 04 1800
* Mayasdfjkljw; 19 2022

Invalid date formats include:
* January 12, 2000 (do not use commas or other punctuation)
* 03 Nov 2020 (use a month-day-year format)
* 10 04 2020 (do not use a numerical representation for the month)
* Apr 11 95 (use a four-digit year)

### Input validation

Date formatting is not validated.
Invalid formats are likely to raise exceptions or cause unexpected behavior.

The existence of given dates *is* validated,
and nonexistent dates will raise an exception.

February 29 will only be considered a valid date for a leap year.

Examples of nonexistent dates include:
* January 32, 2000
* Feb 29, 2000
* April 31, 2000