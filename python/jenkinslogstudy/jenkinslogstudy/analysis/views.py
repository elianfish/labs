import json
import logging
from django.middleware.csrf import get_token
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.utils.encoding import smart_text

from .models import Business,BusinessHistory
# Create your views here.

logger = logging.getLogger('django')


def index(request):
    if not is_login(request):
        return redirect('login')

    user_name = request.session.get('user_name')
    data = Business.objects.filter(user=user_name).order_by('-id')

    return render(request,'index.html', {'data': data})


def do_new_business(request):
    if not is_login(request):
        return redirect('login')

    req = request.REQUEST
    job_name = req['job_name']

    if not job_name:
        msg = 'job name empty'
        return redirect_to_op_result(reqeust, False, msg)

    business = Business()
    business.jenkins_job_name = job_name

    business.save()

    return redirect_to_op_result(request, True)


def login(request):
    result = {
        'user': None,
    }

    if request.method == 'POST':
        data = json.loads(smart_text(request.body))
        form = AuthenticationForm(
            request,
            data=data)
        if form.is_valid():
            logger.debug('login form valid')
            auth_login(request, form.get_user())
            result = {
                'user': {
                    'id': form.get_user().id,
                    'username': form.get_user().get_username(),
                    'displayName': form.get_user().first_name,
                }
            }
            response = JsonResponse(result)
            _set_login_cookie(response, request)
            return response
        else:
            logger.debug('login form invalid, error: %s', form.errors)
    else:
        if request.user.is_authenticated:
            result['user'] = {
                'id': request.user.id,
                'username': request.user.get_username(),
                'displayName': request.user.first_name,
            }
            response = JsonResponse(result)
            _set_login_cookie(response)
            return response

    return JsonResponse(result)


def _set_login_cookie(response, request):
    crsftoken = get_token(request)
    response.set_cookie(
        'cilogin',
        1,
        max_age=settings.SESSION_COOKIE_AGE)
    response.set_cookie('csrftoken', crsftoken, max_age=settings.SESSION_COOKIE_AGE)


def is_login(request):
    is_authenticated = request.user and request.user.is_authenticated
    result = {
        'is_authenticated': is_authenticated
    }
    return JsonResponse(result)