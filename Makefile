.PHONY: clean

clean:
	find . -name "*.o" -or -name "*.cmx" -or -name "*.cmi" -or -name "*.cmo" -or -name "*.out" | xargs rm -f;

DAY = $(shell date +%-d)

deltmp:
	find . -name "part*.*" | xargs rm -f;

pyrun:
	python3 $(DAY)/final.py;

mlrun:
	ocamlopt -o $(DAY)/final.out $(DAY)/final.ml;
	$(DAY)/final.out;
	make clean;

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