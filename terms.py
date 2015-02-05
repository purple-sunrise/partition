#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse


def get_terms_ways_count(n, k, prev=0, level=0):
    count = 0
    a = n - k + 1
    while a >= (n / k if k else 1):
        if prev and a > prev:
            a -= 1
            continue
        if not k == 1 and n > 1:
            count += get_terms_ways_count(n - a, k - 1, a, level + 1)
        else:
            count += 1
        a -= 1
    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        help='the number (should be less than 150)',
        type=int,
        required=True
    )
    parser.add_argument(
        '-k',
        help='the number of terms (should be less than 150)',
        type=int,
        required=True
    )
    args = parser.parse_args()
    if not 0 < args.n <= 150 or not 0 < args.k <= 150:
        print('Wrong init parameters')
        exit(0)
    if args.k > args.n:
        print('Mission is impossible')
        exit(0)
    result = get_terms_ways_count(args.n, args.k)
    print('Result: {0}'.format(result))
