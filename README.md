# csv2bib.py
In bibliographic data such as Scopus and Web of Science, the article search can be export in CSV files. These files are easy to edit in software like Microsoft Excel and Google Sheets. However, in the case of bibliometric analysis exist specialized software, but it receives the information in BibTeX format.

[![Gittip](https://img.shields.io/badge/Latest%20stable-2.1-green.svg?style=flat-squared)]()

# Requirements

- python 3.X or above to run

# How do I use?

1. Dowload the last release;
2. Make the command:

## Running with args in command line
```
python csv2bib.py [csv filename] [bib filename] [database name]

Example: python csv2bib.py Example.csv Example.bib scopus
```

 # Tips
## About the parameters

**--help** or *-h*: Display the commands available.

**[csv filename]**: The path or filename of the input file. (required)

**[bib filename]**: The path or filename of the output file. (required)

**[database name]**: scopus or wos. (required)

## Digital Libraries available
- Scopus
- Web of Science

## Header of CSV
**momentarily** The header must be:

AU  TI  SO  AB  DE  DT  TC  DI  DB  PY  RP  AU_UN WC  ID

