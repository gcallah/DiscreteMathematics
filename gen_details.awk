#!/usr/bin/awk -f

# This program generates the chapter details for 
#  discrete mathematics.
# It reads stdin for the details.

BEGIN {
    curr_file = ""
    indent1 = "    "
    indent2 = indent1 indent1
    indent3 = indent2 indent1
    indent4 = indent2 indent2
}

/^$/ { }       # blank lines allowed

/^\;/ { }      # allows comments in the chapter file

/ptml/ {   # a new file
    curr_file = $0 ".details"
    print "" > curr_file  # truncate file: this might have been
                          # run previously
}

/^[A-Z]/ {     # this is the name of a chapter subsection
    print indent3 "<details>" >> curr_file
    print indent4 "<summary class=\"sum1\">" >> curr_file
    print indent4 $0 >> curr_file
    print indent4 "</summary>" >> curr_file
    print indent3 "</details>" >> curr_file
    print "" >> curr_file
}

