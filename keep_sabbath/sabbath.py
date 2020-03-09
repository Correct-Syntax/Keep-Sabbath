# Keep-Sabbath  Copyright (c) 2019-2020 Correct Syntax, Noah Rahm.
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:

#     1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.

#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.

#     3. The names of Correct Syntax and Noah Rahm may not be used to endorse
#        or promote products derived from this software without specific prior
#        written permission.

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

from datetime import date
from functools import wraps

import requests
from django.shortcuts import render, redirect
from django.conf import settings 



def _sabbath_override():
    """ Sabbath override for Holy Days, etc. when it needs 
    to be overridden to be True (this does not currently work 
    if you need to override it be False). This is not to be 
    used directly, but is used by the is_sabbath function. 
    Returns a boolean value.
    =================================
    Usage:
        This should not be called directly.
    =================================  
    """
    override_is_sabbath = False
    try:
        if settings.IS_SABBATH_OVERRIDE != False:
            override_is_sabbath = True
    except:
        raise ValueError(
            'You have not set the IS_SABBATH_OVERRIDE in your settings.py'
            )
    return override_is_sabbath


def _calculate_time_of_sabbath():
    ## Call api
    data_string = 'https://api.sunrise-sunset.org/json?lat={}?lng={}'.format(
        settings.SABBATH_COORDS_LATITUDE,
        settings.SABBATH_COORDS_LONGITUDE
        )
    response = requests.get(data_string)

    print(response['results']['sunrise'])

    return False


def is_sabbath():
    """ Callable function for determining whether
    the current day and time is the Sabbath or not.
    This is based on an understanding that the Sabbath
    day starts at sundown and ends at sundown the next 
    day. Returns a boolean value.
    =================================
    Usage:
        if is_sabbath() == True:
            ...
    =================================
    """
    is_sabbath_value = False

    # See if it is currently the 6th or 7th day
    weekday = date.today().weekday()
    #print(weekday)
    if weekday not in [4, 5]:
        is_sabbath_value = False
    else:
        #print("yes")
        #is_sabbath_value = _calculate_time_of_sabbath()

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
    =================================
    Usage:
        @redirect_if_sabbath
        def my_view(request):
            ...
    =================================
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
