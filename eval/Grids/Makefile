
all: main
	echo "done"

main: *.tex
	pdflatex -shell-escape -jobname="grids" grids.tex
	pdflatex -shell-escape -jobname="grids" grids.tex
# 	pdftk grids.pdf cat 1-8 9east 10-18 19east 20-end output output.pdf

grayscale:
	gs -sOutputFile=grids-grayscale.pdf -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH grids.pdf
	


clean:
	rm -f grids.pdf
	rm -f *.idx *.aux* *.log *.nav *.out *.snm *.toc *.glo *.gls *.glg *.ist *.xdy *.acn *.acr *.alg *.bbl *.maf *.mtc* *.pyg *.blg *.glsdefs *.mathacr *.mathacn *.md5
