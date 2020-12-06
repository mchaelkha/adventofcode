#!/usr/bin/env bash
mkdir $1
for i in `seq 1 25`; do
	touch $1/d${i}.py
done
