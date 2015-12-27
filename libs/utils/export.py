# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import codecs
import datetime

from django.http import HttpResponse


def null_csv_response():
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8)
    response['Content-Disposition'] = 'attachment; filename="null.csv"'
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
        self.writer.writerow(self.header)  # Write headers to CSV

    def _write_filename(self, filename):
        assert isinstance(filename, basestring), 'filename must be string'
        now = datetime.datetime.now()
        self.response['Content-Disposition'] = 'attachment; filename="%s-%s.csv"' % (filename, now.microsecond)

    def write_row(self, row):
        self.writer.writerow(row)

    def write_rows(self, rows):
        assert hasattr(rows, '__iter__'), 'rows must be iterable'
        for row in rows:
            self.writer.writerow(row)

    def csv_response(self):
        return self.response
