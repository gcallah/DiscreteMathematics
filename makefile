# Need to export first two as ENV var
export TEMPLATE_DIR = templates
export QUIZ_DIR = quizzes
export UTIL_DIR = ./utils

HTMLFILES = $(shell ls *.ptml | sed -e 's/ptml/html/g')
INCS = $(TEMPLATE_DIR)/menu.txt
 
%.html: %.ptml $(INCS)
	python3 $(UTIL_DIR)/html_checker.py $<
	$(UTIL_DIR)/html_include.awk <$< >$@
	git add $@

website: $(HTMLFILES) $(INCS)
	-git commit -a -m "Website rebuild."
	git push origin master

tests: $(QUIZ_DIR)
	cd $(QUIZ_DIR) ; make all

local: $(HTMLFILES)

clean:
	touch *.ptml
	cd $(QUIZ_DIR) ; make clean
