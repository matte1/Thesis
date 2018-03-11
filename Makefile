all:
	pdflatex main.tex
	bibtex main.aux
	pdflatex main.tex

clean:
	rm -f main.log main.aux main.pdf main.toc main.out main.lof main.run.xml \
	  main.lot main-blx.bib main.bbl main.blg Chapters/*.aux Chapters/*.bbl \
		Chapters/*.blg Appendices/*.aux
