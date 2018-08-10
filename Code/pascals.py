#!/usr/bin/python

from sys import argv

sp_per_entry = 5

trows= []

def format_row(row):
    s = ""
    for num in row:
        n = str(num)
        pad = 0
        if len(n) < sp_per_entry:
            pad = sp_per_entry - len(n)
        s += str(num) + (" " * pad)
    return s


def create_triangle(rows=10, m=None):
    prow = None
    for row in range(0, rows + 1):
        print("Calculating row " + str(row))
        entries = row + 1
        nrow = []
        trows.append(nrow)
        for k in range(0, entries):
            if (k == 0) or (k == entries - 1):
                nrow.append(1)
            else:
                k = prow[k - 1] + prow[k]
                if m is not None:
                    k %= m
                nrow.append(k)
        prow = nrow


def output_triangle():
    num_rows = len(trows)
    row_width = (num_rows + 1) * sp_per_entry
    for row in trows:
        padamt = row_width - (len(row) * sp_per_entry) / 2
        padding = " " * padamt
        print(padding + format_row(row) + padding)


if __name__ == "__main__":
    mod = None
    rows = 10
    if len(argv) > 1:
        rows = int(argv[1])
    if len(argv) > 2:
        mod = int(argv[2])
    if rows > 12 and mod is None:
        sp_per_entry += 1
    if rows > 19 and mod is None:
        sp_per_entry += 1
    create_triangle(rows, mod)
    output_triangle()
