clean:
	find . -name "*.o" -or -name "*.cmx" -or -name "*.cmi" -or -name "*.cmo" -or -name "*.out" | xargs rm -f;

deltmp:
	find . -name "part*.*" | xargs rm -f;

pyrun:
	python3 $(DAY)/final.py

mlrun:
	ocamlopt -o $(DAY)/final.out $(DAY)/final.ml
	$(DAY)/final.out
	make clean