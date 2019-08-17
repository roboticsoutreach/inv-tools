#!/usr/bin/env bash

echo "Printing 100 asset labels"
echo "Please check that all printed as expected."

python3 gen-code.py | tee /tmp/codes.csv

echo "Generating PDF"

glabels-3-batch template.glabels -i /tmp/codes.csv -o /tmp/codes-output.pdf

echo "Printing."

lpr -P DYMO-LabelWriter-450 /tmp/codes-output.pdf
