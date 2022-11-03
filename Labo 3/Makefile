all: tp
	echo "done"


tp: *.tex
	pdflatex -shell-escape -jobname="4eisa40_traitement-images_labo3" 4eisa40_traitement-images_labo3.tex
	pdflatex -shell-escape -jobname="4eisa40_traitement-images_labo3" 4eisa40_traitement-images_labo3.tex

clean:
	rm -f  4eisa40_traitement-images_labo3.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc
