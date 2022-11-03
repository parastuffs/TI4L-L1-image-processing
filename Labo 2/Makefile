all: tp
	echo "done"


tp: *.tex
	pdflatex -shell-escape -jobname="4eisa40_traitement-images_labo2" 4eisa40_traitement-images_labo2.tex
	pdflatex -shell-escape -jobname="4eisa40_traitement-images_labo2" 4eisa40_traitement-images_labo2.tex

clean:
	rm -f  4eisa40_traitement-images_labo2.pdf
	rm -f *.idx *.aux *.log *.nav *.out *.snm *.toc
