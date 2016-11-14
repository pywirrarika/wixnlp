# wixnlp 

* **Version:** 0.1
* **Licence:** GPL v.3
* **Author:** Jesús Mager Mager Hois

**wixnlp** is a collection of tools to work with the indigenous language wixárika (huichol), as well chunk of gram and corpus data of the language. The tools are design as a first NLP approach for wixárika language, and can be used easily from command prompt. This tools are used by an [wixárika - spanish translator] (http://turing.iimas.unam.mx), developed at UNAM and UAM universities.
The tools are written in Python with an GPLv3 Licence, so feel free to hack on the code! 

## Usage

To segment a wixarika word use _wmorph.py_
```
$./wmoph.py word
```
From an paried translation file _name.wixes_, sep.py can split the file in to independent files _name.wix_ and _name.es_. This files are used by **Moses** for translation.

File example (corpus.wixes):
```
p+-mexa=es una mesa
p+-xupureru=es un sombrero
p+-p+teya=es una botella
p+-tek+xi=es un vaso
p+-wiki=es un pájaro
p+-ts+k+=es un perro
p+-mitsu=es un gato
p+-muxa=es un borrego
```
To split the file use:
```
$./tools/sep.py -s corpus
```
To merge an wix and an es file in to .wixes:
```
$./tools/sep.py -m corpus
```


## Example

## Citation


