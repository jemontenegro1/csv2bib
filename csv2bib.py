#   Creator:    Elias Munoz Montenegro 
#   email:      jemontenegro@uninorte.edu.co
#   version:    0.1
#   Created:    4th / March / 2020

import sys

def scopusbibentry(Author1,List,Header):
    bibentry = '@ARTICLE{'+Author1+''+List[Header[8]]+',\n'
    bibentry+= 'author={'+List[Header[0]]+'},\n'
    bibentry+= 'title={'+List[Header[1]]+'},\n'
    bibentry+= 'journal={'+List[Header[2]]+'},\n'
    bibentry+= 'year={'+List[Header[8]]+'},\n'
    bibentry+= 'doi={'+List[Header[7]]+'},\n'
    bibentry+= 'note={cited By '+List[Header[6]]+'},\n'
    bibentry+= 'affiliation={'+List[Header[10]]+'},\n'
    bibentry+= 'abstract={'+List[Header[3]]+'},\n'
    bibentry+= 'author_keywords={'+List[Header[4]]+'},\n'
    bibentry+= 'document_type={'+List[Header[5]]+'},\n'
    bibentry+= 'source={'+List[Header[9]]+'},\n'
    bibentry+= '}'
    return bibentry

def wosbibentry(Author1,List,Header):
    bibentry = '@ARTICLE{'+Author1+''+List[Header[8]]+',\n'
    bibentry+= 'author={'+List[Header[0]]+'},\n'
    bibentry+= 'title={'+List[Header[1]]+'},\n'
    bibentry+= 'journal={'+List[Header[2]]+'},\n'
    bibentry+= 'year={'+List[Header[8]]+'},\n'
    bibentry+= 'doi={'+List[Header[7]]+'},\n'
    bibentry+= 'Times-Cited={'+List[Header[6]]+'},\n'
    bibentry+= 'affiliation={'+List[Header[10]]+'},\n'
    bibentry+= 'abstract={'+List[Header[3]]+'},\n'
    bibentry+= 'Keywords={'+List[Header[4]]+'},\n'
    bibentry+= 'Keywords-Plus={'+List[Header[12]]+'},\n'
    bibentry+= 'Web-of-Science-Categories={'+List[Header[11]]+'},\n'
    bibentry+= 'document_type={'+List[Header[5]]+'},\n'
    bibentry+= 'source={'+List[Header[9]]+'},\n'
    bibentry+= '}'
    return bibentry

def csv2bib(filein, fileout,dbtype):
    if '.txt' in filein:
        separator = '\t'
    if '.csv' in filein:
        separator = '","'
    try:
        fi = open(filein,mode='r')
    except FileNotFoundError:
        print('No fue encontrado el archivo', filein)
        exit()
    fo = open(fileout,'w')
    fo.writelines('% Created by csv2bib.py\n')
    fo.writelines('% '+dbtype+' style\n')
    count = 0
    print('Initializing')
    for i, line in enumerate(fi):
        line = line.replace('\n','')
        if not separator == '","':
            line = line.replace('"','')
        List = line.split(sep=separator)
        if i == 0:
            Header = []
            Header.append(List.index('AU'))        #0
            Header.append(List.index('TI'))        #1    
            Header.append(List.index('SO'))        #2
            Header.append(List.index('AB'))        #3
            Header.append(List.index('DE'))        #4
            Header.append(List.index('DT'))        #5
            Header.append(List.index('TC'))        #6
            Header.append(List.index('DI'))        #7
            Header.append(List.index('PY'))        #8
            Header.append(List.index('DB'))        #9
            Header.append(List.index('AU_UN'))     #10
            if dbtype == 'wos':
                Header.append(List.index('WC'))    #11
                Header.append(List.index('ID'))    #12
        else:
            count += 1
            Authors = List[Header[0]]
            Authors = Authors.replace('"','')
            Authors = Authors.replace(';',' and ')
            Author1 = Authors.split(sep=' ')
            if dbtype == 'scopus':
                bibentry = scopusbibentry(Author1[0],List,Header)
            if dbtype == 'wos':
                bibentry = wosbibentry(Author1[0],List,Header)
            fo.writelines('\n'+bibentry+'\n')
            if count%100 == 0:
                print('Article Extracted: ',count)
    print('Article Extracted: ',count)
    fo.close()
    fi.close()

if len(sys.argv) == 1:
    print('Arguments required!')
    print('\tto help use -h or --help')
if len(sys.argv) == 2:
    if '--help' in str(sys.argv[1]) or '-h' in str(sys.argv[1]):
        print('csv2bib help')
        print('Usage: python csv2bib.py [csv filename] [bib filename] [database name]')
        print('Example: python csv2bib.py Example.csv Example.bib scopus')
if len(sys.argv) == 4:
    filein = str(sys.argv[1])
    fileout = str(sys.argv[2])
    dbtype = str(sys.argv[3])
    if not '.csv' in filein and not '.txt' in filein:
        filein = filein+'.txt'
    if not '.bib' in fileout:
        fileout = fileout+'.bib'
    csv2bib(filein,fileout,dbtype)
