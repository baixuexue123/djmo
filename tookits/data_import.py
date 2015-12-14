# -*- coding: utf-8 -*-

""" 构造数据库数据 """

import os
import time
import functools
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "www.settings")

# Django 版本>=1.7时，需要加下面两句,否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
import django
if django.VERSION >= (1, 7):
    django.setup()

from interface_dpi.models import DpiTagJrCellOutput
from interface_phone_dog.models import Task, RePhone
from syndra.models import TaskSyndra


def clock(ms=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            st, st_c = time.time(), time.clock()
            ret = func(*args, **kwargs)
            print 'run time: %.1fms' % ((time.time()-st)*1000) if ms else 'run time: %.4fs' % (time.time()-st)
            print 'cpu time: %.1fms' % ((time.clock()-st_c)*1000) if ms else 'cpu time: %.4fs' % (time.clock()-st_c)
            return ret
        return wrapper
    return decorator


def group_generator(data, chunksize):

    """将迭代器分组返回"""

    chunk = []
    for d in data:
        chunk.append(d)
        if len(chunk) == chunksize:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


@clock(ms=True)
def import_db():
    dpi_data = [
        DpiTagJrCellOutput(
            webid='webid81723hjdh123sdasd',
            user_agent='user_agent',
            contact='13101975598',
            contact_seq='seq',
            credit='65',
            contact_num=5,
            tag_num_rela=1,
            tag_num=1,
            jinrong_id=1,
            baoxian_id=0,
            jinrong_tag='jinrong_tag',
            baoxian_tag='baoxian_tag',
            tag_num_yiwai=2,
            tag_num_shouxian=2,
            tag_num_jiankang=2,
            tag_num_lvyou=2,
            tag_num_chexian=2,
            tag_num_p2p=2,
            tag_num_cf=2,
            tag_num_card=2,
            tag_num_fangchan=2,
            tag_num_qiche=2,
            date='20151209',
            region='0911'
        ) for i in xrange(100000)
    ]
    for group in group_generator(iter(dpi_data), 1000):
        DpiTagJrCellOutput.objects.bulk_create(group)


for group in group_generator(RePhone.objects.filter(task=17).all().iterator(), 100):
    for g in group:
        g.read_status = 1
        g.phone_status = 1
        g.dial_count = 1
        g.class_field = random.choice([1, 2, 3, 4, 5, 6, 10])
        g.save()

#
# RePhone.objects.filter(task=17).update(
#     read_status=1,
#     phone_status=1,
#     dial_count=1,
#     class_field=1
# )


if __name__ == '__main__':
    pass
    # import_db()
