#!/usr/bin/env python
# -*- coding:utf-8 -*-


def theif():
    for x in range(0, 4):
        dis_a = 1 if (x != 0) else 0
        dis_b = 1 if (x == 2) else 0
        dis_c = 1 if (x == 3) else 0
        dis_d = 1 - dis_c

        if ((dis_a + dis_b + dis_c + dis_d) == 3):
            print("This thief is " + chr(ord('A') + x))
            break


def main():
    theif()


if __name__ == '__main__':
    main()
