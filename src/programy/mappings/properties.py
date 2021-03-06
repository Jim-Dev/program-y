"""
Copyright (c) 2016 Keith Sterling

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from programy.mappings.base import DoubleStringCharSplitCollection

class PropertiesCollection(DoubleStringCharSplitCollection):

    def __init__(self):
        DoubleStringCharSplitCollection.__init__(self)

    def get_split_char(self):
        return ":"

    def split_line(self, line):
        splits = self.split_line_by_char(line)
        if len(splits) > 2:
            return [splits[0], self.get_split_char().join(splits[1:])]
        else:
            return splits

    def has_property(self, key):
        return self.has_key(key)

    def property(self, key):
        return self.value(key)

    def add_property(self, key, value):
        if self.has_property(key):
            self.set_value(key, value)
        else:
            self.pairs.append([key, value])
