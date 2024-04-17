FILENAME = Networking
PROJ_DIR := $(CURDIR)
BUILD_DIR = $(CURDIR)/build

# pdf:
# 	pandoc $(FILENAME).md \
# 		--to=latex \
#     	--output=$(BUILDDIR)/$(FILENAME).pdf header.yml\
#     	--pdf-engine=xelatex
#     	# --filter pandoc-citeproc \
#     	# --from=markdown+tex_math_single_backslash+tex_math_dollars+raw_tex \

# $(info $$PROJ_DIR is [${PROJ_DIR}])


pdf:
	pdflatex -shell-escape -s $(PROJ_DIR)/$(FILENAME).tex \
    	 --output=$(BUILDDIR)/$(FILENAME).pdf $(PROJ_DIR)/header.yml
		#  -output-directory=$(BUILD_DIR)
		# --pdf-engine=xelatex
    	# --filter pandoc-citeproc \
    	# --from=markdown+tex_math_single_backslash+tex_math_dollars+raw_tex \
    	
clean:
	rm -f *.pdf *.aux *.log *.toc *.blg *.out *.bbl