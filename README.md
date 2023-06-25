# Inv Tools

'Temporary' Inventory Tooling

The SRO asset tag system

## How to Use

1. Generate some codes with `gen_code.py`  
   ```sh
   python3 gen_code.py 10 --prefix BB > codes.csv
   ```
2. Merge them into the label template `template.glabels`  
   1. Run `glabels-qt` and open `template.glabels`
   2. Select the 'Merge' tab.  
   3. For the format, choose plain CSV and then browse for `codes.csv` from step 1.
3. Print them on Dymo 25x54mm Durable labels  
   Connect the printer and print from the 'print' tab in gLabels.

## Installing

The Python scripts depend only on [damm32 1.0.0](https://pypi.org/project/damm32/1.0.0/).

```sh
pip install -r requirements.txt
```

Rendering the template requires [gLabels 4](http://glabels.org/) and [qrencode](https://fukuchi.org/works/qrencode/index.html.en).
qrencode can be had from your favourite package manager. To install gLabels, follow the [instructions on the GitHub page](https://github.com/jimevins/glabels-qt#download).
For the QR codes to work, you might have to first install qrencode, then compile gLabels from source.
