# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BlockedIpMiddleware(object):

    def process_request(self, request):
        print '-------------------------------------------'
        print request.META['REMOTE_ADDR']
        print '-------------------------------------------'
