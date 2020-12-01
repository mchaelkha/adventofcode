#!/usr/bin/env bash
for i in `seq 1 25`; do
	mkdir d${i}
	touch d${i}/p1.py
	touch d${i}/p2.py
done
