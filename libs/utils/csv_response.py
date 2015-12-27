# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import csv
import codecs
import cStringIO

from django.http.response import StreamingHttpResponse, HttpResponse
from django.views.generic import View


class CSVResponseMixin(object):

    csv_filename = 'null.csv'
    csv_header = []

    def get_csv_filename(self):
        return self.csv_filename

    def render_to_csv(self, data):
        response = HttpResponse(content_type='text/csv')
        response.write(codecs.BOM_UTF8)
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(self.get_csv_filename())
        # Write data to CSV
        writer = csv.writer(response)
        writer.writerow(self.csv_header)
        for row in data:
            writer.writerow(row)
        return response


class DataView(CSVResponseMixin, View):

    def get(self, request, *args, **kwargs):
        data = (('hello', 'world'), ('foo', 'bar'))
        return self.render_to_csv(data)


# 流式响应StreamingHttpResponse可以快速,节省内存地产生一个大型文件
class Echo(object):

    def write(self, value):
        return value


class UnicodeWriter(object):

    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding='utf-8', **kwargs):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwargs)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([handle_column(s) for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        value = self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
        return value

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


class ExampleView(View):

    headers = ('一些', '表头')

    def get(self, request):
        result = (
            ('第一行', '数据1'),
            ('第二行', '数据2')
        )
        echoer = Echo()
        writer = UnicodeWriter(echoer)

        def csv_iterator():
                yield codecs.BOM_UTF8
                yield writer.writerow(self.headers)
                for column in result:
                    yield writer.writerow(column)

        response = StreamingHttpResponse(
                (row for row in csv_iterator()),
                content_type="text/csv;charset=utf-8"
        )
        response['Content-Disposition'] = 'attachment;filename="example.csv"'
        return response
