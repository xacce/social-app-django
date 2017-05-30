import json
import six
import functools

import django

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.postgres.fields import JSONField

try:
    from django.utils.encoding import smart_unicode as smart_text

    smart_text  # placate pyflakes
except ImportError:
    from django.utils.encoding import smart_text

# SubfieldBase causes RemovedInDjango110Warning in 1.8 and 1.9, and
# will not work in 1.10 or later
if django.VERSION[:2] >= (1, 8):
    field_metaclass = type
else:
    from django.db.models import SubfieldBase

    field_metaclass = SubfieldBase

field_class = functools.partial(six.with_metaclass, field_metaclass)
