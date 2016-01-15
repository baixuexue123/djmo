# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import codecs
import datetime

from django.http import HttpResponse
from django.views.generic import View


def null_csv_response():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="null.csv"'
    return response


def render_csv_response(filename, data, header=None):
    assert hasattr(data, '__iter__'), 'data must be iterable'
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
    writer = csv.writer(response)
    if header:
        writer.writerow(header)
    for row in data:
        writer.writerow(row)
    return response


class ExportCsv(object):
    """
    Export csv
    """

    header = []

    def __init__(self, filename):
        self.response = HttpResponse(content_type='text/csv')
        self.response.write(codecs.BOM_UTF8)
        self._write_filename(filename)
        self.writer = csv.writer(self.response)
        self.writer.writerow(self.header)  # write headers to CSV

    def _write_filename(self, filename):
        now = datetime.datetime.now()
        self.response['Content-Disposition'] = 'attachment; filename="%s-%s.csv"' % (filename, now.microsecond)

    def write_row(self, row):
        self.writer.writerow(row)

    def write_rows(self, rows):
        assert hasattr(rows, '__iter__'), 'rows must be iterable'
        for row in rows:
            self.write_row(row)

    def csv_response(self):
        return self.response


class CSVResponseMixin(object):

    csv_filename = 'null.csv'
    csv_header = []

    def get_csv_filename(self):
        return self.csv_filename

    def render_to_csv(self, data):
        response = HttpResponse(content_type='text/csv')
        response.write(codecs.BOM_UTF8)
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(self.get_csv_filename())
        writer = csv.writer(response)
        writer.writerow(self.csv_header)
        for row in data:
            writer.writerow(row)
        return response


class CSVResponseMixinExampleView(CSVResponseMixin, View):

    def get(self, request, *args, **kwargs):
        data = (('hello', 'world'), ('foo', 'bar'))
        return self.render_to_csv(data)
