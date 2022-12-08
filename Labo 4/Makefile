all: tp
	echo "done"


tp: *.tex
	pdflatex -shell-escape -jobname="4eisa40_traitement-images_labo4" 4eisa40_traitement-images_labo4.tex
	pdflatex -shell-escape -jobname="4eisa40_traitement-images_labo4" 4eisa40_traitement-images_labo4.tex

clean:
	rm -f  4eisa40_traitement-images_labo4.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc
