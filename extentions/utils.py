from . import jalali
from django.utils import timezone


def to_jalali(time):
    time = timezone.localtime(time)
    calender_to_str = datetime_to_str(time)
    jalali_format = jalali.Gregorian(calender_to_str).persian_tuple()
    month_name = mounth_number_to_name(jalali_format[1])
    combined_str = "{} {} {}, ساعت {}:{}".format(
        jalali_format[2],
        month_name,
        jalali_format[0],
        time.hour,
        time.minute,
    )
    final_str = en_to_fa_numbers(combined_str)
    return final_str


def datetime_to_str(dt):
    result = "{}-{}-{}".format(
        dt.year,
        dt.month,
        dt.day,
    )
    return result


def mounth_number_to_name(number):
    months = [
        "",
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]
    for index, m in enumerate(months):
        if number == index:
            return m


def en_to_fa_numbers(strNumber):
    en_to_fa_dictionary = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    for e, p in en_to_fa_dictionary.items():
        strNumber = strNumber.replace(e, p)
    return strNumber
