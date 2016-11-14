<img src="https://raw.githubusercontent.com/pywirrarika/wixnlp/master/tools/wixnlp.png" width=250px>

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
'ena ha p+xuawe=aquí hay agua
'ena ha p+yema=aquí está el agua
'ena ha p+kamawe=aquí no hay agua
'ena ha p+kaxuawe=aquí no hay agua
'ena ha p+kayema=aquí no está el agua
```
To split the file use:
```
$./tools/sep.py -s corpus
```
To merge an wix and an es file in to .wixes:
```
$./tools/sep.py -m corpus
```
To normalize and tokenize
```
$./normwix.py corpus.wix
```

And to segment, and anotate a entire file:
```
$./wixpre.py corpus.wix
'ena ha p+3 xuawe
'ena ha p+3 ye15 ma
'ena ha p+3 ka4 mawe
'ena ha p+3 ka4 xuawe
'ena ha p+3 ka4 ye15 ma
```

## Citation

You are welcome to use the code under the terms for research or commercial purposes, however please acknowledge its use with a citation:
Mager Jesus, Barron Carlos and Meza Ivan. "Traductor estadístico wixarika - español usando descomposición morfológica", COMTEL,  number 6, September 2016.
Here is a BiBTeX entry:

```
@article{tradmager,
author = "Mager Hois, Jesús Manuel and Barron Romero, Carlos and Meza Ruíz, Ivan Vladimir",
journal = "COMTEL",
number = "6",
title = "Traductor estadístico wixarika - español usando descomposición morfológica",
year = "2016",
month = sep
}

```

