.PHONY: clean

clean:
	find . -name "*.o" -or -name "*.cmx" -or -name "*.cmi" -or -name "*.cmo" -or -name "*.out" | xargs rm -f;