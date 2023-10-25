# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SHELL 			 := /bin/bash
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = ./build/sphinx

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

IPYNB := $(shell find . -name '*.ipynb' -not -path '*/.ipynb_checkpoints/*' | sed 's/.* .*//g')
IPYRST := $(patsubst %.ipynb,%.rst, $(IPYNB))

.PHONY: help clean html livehtml dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest apidoc

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  livehtml   to make standalone HTML files while watching the directory (requires sphinx-autobuild)"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"

clean:
	-rm -rf $(BUILDDIR)/*
	-rm -rf docs/_autosummary/

livehtml:
	sphinx-autobuild --ignore '*.#*' --ignore '_autosummary' --ignore '*.pyc' --ignore '*.swp' --ignore '*.swo' -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html/docs --host='*' #--open-browser

livehtml-theme:
	sphinx-autobuild -a --watch '_templates' --watch '_static' --ignore '_autosummary' --ignore '*.#*' --ignore '*.pyc' --ignore '*.swp' --ignore '*.swo' -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html/docs --host='*' #--open-browser

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html --color 2> >(tee html-build.log >&2)
	cat html-build.log | aha -b > build/sphinx/html/html-build.log.html
	# strip the ANSI codes
	sed -i -e 's/\x1b\[[0-9;]*m//g' html-build.log
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

optimizer-dcc:
	$(SPHINXBUILD) -D master_doc="optimizer/overview" -E -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/optimizer-dcc
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/Pyro.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/Pyro.qhc"

devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/Pyro"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/Pyro"
	@echo "# devhelp"

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	make -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

apidoc:
	sphinx-apidoc -o apidoc/pytest/ --implicit-namespaces ../wield-pytest/src/wield/
	sphinx-apidoc -o apidoc/bunch/ --implicit-namespaces ../wield-bunch/src/wield/
	sphinx-apidoc -o apidoc/utilities/ --implicit-namespaces ../wield-utilities/src/wield/
	sphinx-apidoc -o apidoc/quantum/ --implicit-namespaces ../wield-quantum/src/wield/
	sphinx-apidoc -o apidoc/control/ --implicit-namespaces ../wield-control/src/wield/
	sphinx-apidoc -o apidoc/devel/ --implicit-namespaces ../wield-devel/src/wield/
	sphinx-apidoc -o apidoc/model/ --implicit-namespaces ../wield-model/src/wield/
	sphinx-apidoc -o apidoc/LIGO-IFO/ --implicit-namespaces ../wield-LIGO-IFO/src/wield/
	sphinx-apidoc -o apidoc/iirrational/ --implicit-namespaces ../wield-iirrational/src/wield/
	sphinx-apidoc -o apidoc/gwinc/ --implicit-namespaces ../pygwinc/test/  ../pygwinc/gwinc/

ipynb: $(IPYRST)

svg-embed: $(SVGVIEW)

%_view.svg: %_embed.svg
	./inkscape/embedimage.py $< > $@

#TODO maybe use a config file for this
%.rst: %.ipynb
	jupyter nbconvert --NbConvertApp.output_files_dir='{notebook_name}-ipynb' --to rst $<

#sed -i '1s;^;#$(<F) [notebook]($(<F))\n;' $@
#jupyter nbconvert --NbConvertApp.output_files_dir='{notebook_name}-ipynb' --to html $<

%.html: %.ipynb
	jupyter nbconvert --NbConvertApp.output_files_dir='{notebook_name}-ipynb' --to html $<
