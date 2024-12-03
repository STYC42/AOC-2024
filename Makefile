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
	find . -name "part*.*" | xargs rm -f;

pyrun:
	python3 $(DAY)/final.py;

mlbuild:
	mkdir -p $(DAY)/bin
	ocamlopt -o $(DAY)/bin/final.out str.cmxa $(DAY)/final.ml
	make clean

mlrun:
	$(DAY)/bin/final.out;

tmp1run:
	python3 $(DAY)/part1.py

tmp2run:
	python3 $(DAY)/part2.py

setup:
	mkdir -p $(DAY);
	cp template.py $(DAY)/part1.py;
	cp template.py $(DAY)/part2.py;
	sed -i "s/{{DAY}}/$(DAY)/g" $(DAY)/part1.py;
	sed -i "s/{{DAY}}/$(DAY)/g" $(DAY)/part2.py;
	aocd $(DAY) > $(DAY)/input.txt;