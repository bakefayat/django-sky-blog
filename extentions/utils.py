from django.http import HttpRequest, HttpResponse
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from .jalali import(
    Gregorian, 
    datetime_to_str, 
    mounth_number_to_name, 
    en_to_fa_numbers
)


def to_jalali(time):
    time = timezone.localtime(time)
    calender_to_str = datetime_to_str(time)
    jalali_format = Gregorian(calender_to_str).persian_tuple()
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


def check_author_staff_superuser(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if (
            request.user.is_superuser
            or request.user.is_staff
            or request.user.is_author
        ):
            return True
    return False


def check_staff_superuser(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if (
            request.user.is_staff
        or request.user.is_superuser
        ):
            return True
    return False


def check_owner_staff_superuser(request: HttpRequest, article) -> HttpResponse:
    if request.user.is_authenticated:
        if (request.user.is_superuser
            or request.user.is_staff
            or request.user.is_author
            and article.author == request.user
            ):
            request.is_ok = True
            return request
    raise PermissionDenied
