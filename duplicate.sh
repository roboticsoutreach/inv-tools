while true; do
	read code
	echo -n $code > codes.csv
	rm -f output.pdf
	echo "Generating"
	glabels-3-batch template.glabels -i codes.csv -o output.pdf
	echo "Generated."
	echo "Printing."
	lpr -P DYMO-LabelWriter-450 output.pdf
	echo "Printed."
done
