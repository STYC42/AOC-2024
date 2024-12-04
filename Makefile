.PHONY: clean

clean:
	find . -name "*.o" -or \
		   -name "*.cmx" -or \
		   -name "*.cmi" -or \
		   -name "*.cmo" -or \
		   \( -name "*.out" -not -path "*/bin/*" \) \
		   | xargs rm -f;

ultraclean:
	find . -name "*.o" -or \
		   -name "*.cmx" -or \
		   -name "*.cmi" -or \
		   -name "*.cmo" -or \
		   -name "*.out" \
		   | xargs rm -f;
	find . -type d -name "bin" | xargs rm -rf;

DAY = $(shell date +%-d)

deltmp:
	find . -name "fast.py" | xargs rm -f;

pyrun:
	python3 $(DAY)/final.py;

mlbuild:
	mkdir -p $(DAY)/bin
	ocamlopt -o $(DAY)/bin/final.out str.cmxa $(DAY)/final.ml
	make clean

mlrun:
	$(DAY)/bin/final.out;

run:
	python3 $(DAY)/fast.py

setup:
	mkdir -p $(DAY);
	cp template.py $(DAY)/fast.py;
	sed -i "s/{{DAY}}/$(DAY)/g" $(DAY)/fast.py;
	aocd $(DAY) > $(DAY)/input.txt;