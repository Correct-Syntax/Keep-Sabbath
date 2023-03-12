# Keep-Sabbath Copyright (c) 2019-2023 Noah Rahm.

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:

#     1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.

#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.

#     3. Neither the name of the copyright holder nor the names of its contributors 
#     may be used to endorse or promote products derived from this software without 
#     specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



"""
Django Keep-Sabbath is for webmasters with e-commerce shops, blogs, etc. who would like to keep the Biblical 7th-day Sabbath and other Holy days of the Bible Holy. 

The app allows you to easily setup a system for a Django-powered website that will automatically redirect visitors to a single page (explaining about the Sabbath, redirect, etc.) if it is the Sabbath day or another Holy day.

The app uses internal, offline calculations (via the SolarTime module) and the current date/time of the server to figure out if it is the Sabbath day (thus, if the user should be redirected), so you do not have to do it manually. 

However, there is an option to manually override it as well, which is useful for other Biblical Holy days.

The timing is based on the understanding that the Sabbath day starts on 6th day ("friday") evening and ends on 7th day ("saturday") evening, according to the Bible.

"If thou turn away thy foot from the sabbath, [from] doing thy pleasure on My holy day; and call the sabbath a delight, the holy of Yahweh, honourable; and shalt honour him, not doing thine own ways, nor finding thine own pleasure, nor speaking [thine own] words:
Then shalt thou delight thyself in Yahweh; and I will cause thee to ride upon the high places of the earth, and feed thee with the heritage of Jacob thy father: for the mouth of Yahweh hath spoken [it]." -Isaiah 58:13-14
"""

import pytz
from datetime import date, datetime, timedelta
from functools import wraps

# Check to see if solartime is installed
try:
    from solartime import SolarTime
except:
    # Fallback on the internal one
    from .vendor.solartime import SolarTime

from django.shortcuts import render, redirect
from django.conf import settings 
from django.utils import timezone


def _sabbath_override():
    """ Sabbath override for Holy Days, etc. when it needs 
    to be overridden to be True (this does not currently work 
    if you need to override it be False). This is not to be 
    used directly, but is used by the is_sabbath function. 
    
    :returns: a boolean value.

    This should not be called directly.
    ===================================  
    """
    override_is_sabbath = False
    try:
        if settings.SABBATH_MANUAL_OVERRIDE != False:
            override_is_sabbath = True
    except:
        raise ValueError(
            'You have not set the IS_SABBATH_OVERRIDE setting in your settings.py'
            )
    return override_is_sabbath


def _get_sunset_time(sun, localtz, day, lat, lng):
    """ Get the sunset time for a paticular location.

    :returns: a datetime object.

    This should not be called directly.
    ===================================  
    """
    schedule = sun.sun_utc(day, lat, lng)
    sunset = schedule['sunset'].astimezone(localtz)
    return sunset


def _is_during_sabbath(sun, rs_sunset_day, s_sunset_day):
    """ Internal function which uses the given data to figure out
    whether it is before, during or after the Sabbath day and returns
    the proper value.

    This should not be called directly.
    ===================================  
    """
    sabbath_start = rs_sunset_day.strftime('%y %m %d %I:%M %p')
    sabbath_end = s_sunset_day.strftime('%y %m %d %I:%M %p')
    now = timezone.now().strftime('%y %m %d %I:%M %p')

    # Uncomment below to manually set a date/time for testing
    # now = datetime(2020, 6, 9, 23, 4, 0, tzinfo=pytz.utc).strftime('%y %m %d %I:%M %p')
    # print(
    #     "sabbath starts: ", sabbath_start, 
    #     "\nsabbath ends: ", sabbath_end, 
    #     "\ndate now: ", now
    #     )

    if sabbath_start < now:
        # We know the sabbath has started
        if sabbath_end < now:
            # Its after the sabbath now
            return False
        else:
            # Its still during the sabbath
            return True 

    elif sabbath_start > now:
         # It is probably before the sabbath
        return False

    else:
        # This shouldn't ever happen... :)
        return False


def _calculate_is_sabbath(weekday):
    """ Internal function to calculate whether it is 
    the Sabbath or not. Same as calling ``is_sabbath``,
    only without the override and performance optimizations.

    This should not be called directly.
    ===================================  
    """

    # 6th day (rev Sabbath, the evening 
    # when the Sabbath starts).
    if weekday == 4: 
        rev_sabbath_day = date.today() 
        sabbath_day = rev_sabbath_day + timedelta(days=1)
    
    # the 7th day (the Sabbath)
    elif weekday == 5: 
        sabbath_day = date.today() 
        rev_sabbath_day = sabbath_day - timedelta(days=1) 
        
    # print(rev_sabbath_day)
    # print(sabbath_day)

    # Use the solartime module to calculate sunsets
    sun = SolarTime()
    localtz = pytz.timezone(settings.SABBATH_LOCAL_TIMEZONE)
    lat  = settings.SABBATH_COORDS_LATITUDE
    lng = settings.SABBATH_COORDS_LONGITUDE

    rs_sunset = _get_sunset_time(sun, localtz, rev_sabbath_day, lat, lng)
    s_sunset = _get_sunset_time(sun, localtz, sabbath_day, lat, lng)

    return _is_during_sabbath(sun, rs_sunset, s_sunset)


def get_weekday():
    """ Get the current day of the week.

    :returns: an integer of 0-6, where "Monday" 
    is 0 and "Sunday" is 6 (weird, isn't?)
    """
    return date.today().weekday()


def is_sabbath():
    """ Callable function for determining whether
    the current day and time is the Sabbath or not.
    This is based on an understanding that the Sabbath
    day starts at sundown and ends at sundown the next 
    day. 

    Usage (in a django view):
        if is_sabbath() is True:
            ...
    
    :returns: a boolean value
    """
    is_sabbath_value = False

    # See if it is currently the 6th or 7th day
    weekday = get_weekday()

    # This is a performance optimization:
    # it will only calculate the sabbath times if it
    # is near the Sabbath Day (rev-shabbat) or the day-of.
    if weekday in [4, 5]:
        is_sabbath_value = _calculate_is_sabbath(weekday)
    else:
        is_sabbath_value = False
    
    # print("Redirect?: ", is_sabbath_value)

    # Check to see if there is an override
    if _sabbath_override() == True:
        return True
    else:
        return is_sabbath_value


def _redirect_if_sabbath():
    """ Django views decorator for redirecting users to the 
    Sabbath redirect page if it is the Sabbath (or if the 
    value is overridden when it is a Holy Day, etc).
    Otherwise, the view's normal page will be returned.

    Please use ``redirect_if_sabbath`` to access this function instead
    of calling this directly.

    Usage (in views.py file):

        @redirect_if_sabbath
        def my_view(request):
            ...
    """
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if is_sabbath() == True:
                return redirect('keep_sabbath:sabbath-redirect')
            return func(request, *args, **kwargs)
        return inner
    return decorator

redirect_if_sabbath = _redirect_if_sabbath()
