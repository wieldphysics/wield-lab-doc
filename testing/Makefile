.PHONY: list print collect

.ONESHELL:

#this is necessary to prevent the "intermediate" report files in the reports directory from being deleted
.SECONDARY:

collect: pytest-collection.txt

pytest-collection.txt:
	pytest  --rootdir='.' -c 'pytest.ini' --ws-co --html='' | tee pytest-collection.txt

coverage: 
		coverage combine --keep test_results/reports/coverage/*
		rm test_results/coverage/* || true
		coverage html -d test_results/coverage/
		# this is a bit hacky I know. Should use a greedy regex or more restrictive
		sed -i -e 's|>/[^<>]*/wield/|>wield/|' test_results/coverage/*.html
		sed -i -e 's|>/[^<>]*/gwinc/|>gwinc/|' test_results/coverage/*.html


TESTS = $(shell python3 -m wield.pytest.parse_collection pytest-collection.txt 2> /dev/null)

$(TESTS): %: test_results/reports/%.html
		@echo $*

test_results/reports/%.html: pytest-collection.txt
		$(eval FILE := $(shell python3 -m wield.pytest.parse_collection pytest-collection.txt $*))
		$(eval PREHTML := test_results/reports/inprogress/$*.html)
		-mkdir -p test_results/reports/inprogress
		ln --force -T -s ../assets test_results/reports/inprogress/assets;
		-mkdir -p test_results/reports/assets
		-mkdir -p test_results/reports/coverage
		#-pytest $(FILE) --ws-skip-slow --html=$(PREHTML)
		# This long command runs the specific pytest and generates a coverage file
		coverage run --source=wield --source=gwinc --branch --context=$* --data-file=test_results/reports/coverage/$* -m pytest -c 'pytest.ini' --rootdir='.' $(FILE) --ws-skip-slow --html=$(PREHTML)
		if [ "$$?" -eq 0 ]; \
    then \
			mv $(PREHTML) $@; \
			ln --force -T -s ../$*.html test_results/reports/all/$*.html; \
		else\
			mkdir -p test_results/reports/failed; \
			mkdir -p test_results/reports/all; \
			ln --force -T -s ../assets test_results/reports/failed/assets; \
			mv $(PREHTML) test_results/reports/failed/; \
			ln --force -T -s ../failed/$*.html test_results/reports/all/$*.html; \
			false; \
    fi


print:
	@echo $(TESTS);


all: $(TESTS)


.DEFAULT_GOAL := all

