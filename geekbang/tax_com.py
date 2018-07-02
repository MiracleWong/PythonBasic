# -*- coding:utf-8 -*-
# personal income tax
# 介绍bisect的文章：https://www.cnblogs.com/skydesign/archive/2011/09/02/2163592.html

import sys
import bisect


def personal_income_tax(salary, exemption):
    if salary < exemption:
        return 0.0

    above = salary - exemption

    ranges = [0, 1500, 4500, 9000, 35000, 55000, 80000]
    rate =   [.03, .1,  .2,  .25,  .30,   .35,   .45]
    i = bisect.bisect_left(ranges, above)
    j = 0
    tax = 0.0
    while j < i:
        if j+1 < i:
            tax += (ranges[j+1]-ranges[j]) * rate[j]
        else:
            tax += (above-ranges[j]) * rate[j]
        j += 1

    return tax

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <salary>".format(sys.argv[0]))
        sys.exit(1)

    salary = float(sys.argv[1])
    old_exemption = 3500
    new_exemption = 5000
    old_tax = personal_income_tax(salary, 3500)
    new_tax = personal_income_tax(salary, 5000)
    bonus = old_tax - new_tax
    print("old: {}, new: {}, bonus: {}, ".format(old_tax, new_tax, bonus))
