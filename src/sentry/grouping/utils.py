from __future__ import absolute_import

from hashlib import md5

from django.utils.encoding import force_bytes

DEFAULT_FINGERPRINT_VALUES = frozenset(['{{ default }}', '{{default}}'])


def hash_from_values(values):
    result = md5()
    for value in values:
        result.update(force_bytes(value, errors='replace'))
    return result.hexdigest()


def get_grouping_family_for_platform(platform):
    if platform in ('objc', 'cocoa', 'swift', 'native', 'c'):
        return 'native'
    if platform in ('javascript', 'node'):
        return 'javascript'
    return 'other'
