#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Author   : lizs
# @Site     : http://www.alizs.cc
# @Time     : 17-7-3 上午12:06


class Algorithm(object):
    def __init__(self):
        pass

    def decimal_to_other(self, decimal, other_system=2):
        """The numbers of decimal convert to other binary, octal or hexadecimal.

        decimal: decimal numbers
        other_system: 2/8/16, binary/octal/hexadecimal
        """
        div = abs(decimal)
        if div and other_system > 0:
            div_list = []
            while div:
                div, mod = divmod(div, other_system)
                print('Div: %s, Mod: %s' % (div, mod))
                div_list.insert(0, mod)
            print(div_list)
            return reduce(lambda x, y: x * 10 + y, div_list)
        return False
