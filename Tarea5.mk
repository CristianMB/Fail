Graficas_CI = HX1.png HX2.png HY1.png HY2.png RMC1.png RMC2.png 
Graficas_RC = VSR.png VSC.png HR.png HC.png MA.png 

Resultados_hw5.pdf : Resultados_hw5.tex $(Graficas_CI) $(Graficas_RC) 
	pdflatex $< $@
	rm -f *.png
	rm -f *.log
	rm -f *.aux

$(Graficas_CI) : plots_canal_ionico.py 
	python $< $@
$(Graficas_RC) : circuitoRC.py CircuitoRC.txt
	python $< $@


