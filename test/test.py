#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Author   : lizs
# @Site     : http://www.alizs.cc
# @Time     : 17-7-3 上午12:41

from algorithm import Algorithm


class Test(object):
    def __init__(self):
        pass

    def test1(self, decimal, system=2):
        result = Algorithm().decimal_to_other(decimal, other_system=system)
        print(result)
        print(divmod(0, 1))
