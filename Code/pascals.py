#!/usr/bin/python

SPACES_PER_ENTRY = 6

trows= []

def format_row(row):
    s = ""
    for num in row:
        n = str(num)
        pad = 0
        if len(n) < SPACES_PER_ENTRY:
            pad = SPACES_PER_ENTRY - len(n)
        s += str(num) + (" " * pad)
    return s


def create_triangle(rows=10, m=1):
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
                nrow.append(prow[k - 1] + prow[k])
        prow = nrow


def output_triangle():
    num_rows = len(trows)
    row_width = (num_rows + 1) * SPACES_PER_ENTRY
    for row in trows:
        padamt = row_width - (len(row) * SPACES_PER_ENTRY) / 2
        padding = " " * padamt
        print(padding + format_row(row) + padding)


if __name__ == "__main__":
    create_triangle()
    output_triangle()
