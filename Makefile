PYTHON        = python3
SPHINXOPTS    =
SVNROOT       = http://svn.python.org/projects
ALLSPHINXOPTS = -b $(BUILDER) -d build/doctrees -D latex_paper_size=$(PAPER) \
                $(SPHINXOPTS) . build/$(BUILDER) $(SOURCES)
SVN           = $(which svn)

# Delete target files if the command fails after it has
# started to update the file.
.DELETE_ON_ERROR:


.DEFAULT: help

.PHONY: help checkout update build doctest clean

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean      to remove build files"
	@echo "  build      to build the project"
	@echo "  update     to update build tools"
	@echo "  doctest    to run doctests in the documentation"

# Note: if you update versions here, do the same in make.bat and README.txt
checkout:
	@if test ! -d tools/sphinx; then \
	  echo "Checking out Sphinx..."; \
	  svn checkout $(SVNROOT)/external/Sphinx-1.2/sphinx tools/sphinx; \
	fi
	@if test ! -d tools/docutils; then \
	  echo "Checking out Docutils..."; \
	  svn checkout $(SVNROOT)/external/docutils-0.11/docutils tools/docutils; \
	fi
	@if test ! -d tools/jinja2; then \
	  echo "Checking out Jinja..."; \
	  svn checkout $(SVNROOT)/external/Jinja2-2.7.2/jinja2 tools/jinja2; \
	fi
	@if test ! -d tools/pygments; then \
	  echo "Checking out Pygments..."; \
	  svn checkout $(SVNROOT)/external/Pygments-1.6/pygments tools/pygments; \
	fi

clean: 
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} + 
	-rm --force --recursive build/
	-rm --force --recursive dist/
	-rm --force --recursive tools/
	-rm --force --recursive *.egg-info

update: clean checkout

build: checkout
	mkdir -p build/$(BUILDER) build/doctrees
	$(PYTHON) setup.py build
	@echo

doctest: BUILDER = doctest
doctest: build
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in build/doctest/output.txt"
