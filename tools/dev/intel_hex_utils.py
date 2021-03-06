"""
Copyright (c) 2014-2019 ARM Limited. All rights reserved.

SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from intelhex import IntelHex
from cStringIO import StringIO


def sections(h):
    start, last_address = None, None
    for a in h.addresses():
        if last_address is None:
            start, last_address = a, a
            continue

        if a > last_address + 1:
            yield (start, last_address)
            start = a

        last_address = a

    if start:
        yield (start, last_address)


def print_sections(h):
    for s in sections(h):
        print "[0x%08X - 0x%08X]" % s


def decode(record):
    h = IntelHex()
    f = StringIO(record)
    h.loadhex(f)
    h.dump()
