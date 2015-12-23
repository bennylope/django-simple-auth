# encoding: utf-8

import re
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.http import urlencode


def allow_user(request):
    if request.user.is_authenticated():
        return True
    if request.session.get('simple_auth'):
        return True
    return False


class SimpleAuthMiddleware(object):

    def process_request(self, request):
        if allow_user(request):
            return None

        IGNORE = getattr(settings, 'SIMPLE_AUTH_IGNORE', [r'^admin/'])
        PROTECT = getattr(settings, 'SIMPLE_AUTH_PROTECT', [])

        if reverse('simple_auth_password') in request.path:
            return None

        # Strip leading slash
        search_path = request.path[1:]

        for ignored_pattern in IGNORE:
            if re.match(ignored_pattern, search_path):
                return None

        if PROTECT:
            for protected_pattern in PROTECT:
                print(protected_pattern, search_path)
                if re.match(protected_pattern, search_path):
                    return redirect("{0}?{1}".format(
                        reverse('simple_auth_password'),
                        urlencode({'url': request.path}),
                    ))
            return None

        return redirect("{0}?{1}".format(
            reverse('simple_auth_password'),
            urlencode({'url': request.path}),
        ))
