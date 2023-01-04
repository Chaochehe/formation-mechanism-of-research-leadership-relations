
import pandas as pd
import os
from parse import saveToMysql as sv


if __name__ == "__main__":
    Folder_Path =  r'wos_data'  
    total_count = 0
    file_dir = Folder_Path
    basic_files = os.listdir(file_dir)
    print(basic_files)

    for basic_file in basic_files:
        print(basic_file) 
        total_count += 1
        for count, line in enumerate(open(Folder_Path + basic_file, 'r', encoding='UTF-16')):
            if total_count >= 0:
                if count > 0: 
                    a = line.split(("\t"))
                    if len(a) > 2:
                        year = ''
                        full_name = ''
                        co_author = ''
                        reprint_author = ''
                        title = ''
                        author_keyword = '0'
                        keyword = ''
                        abstract = ''
                        citation = '0'
                        year = ''
                        doi = ''

                        try:
                            abstract = a[21].split(' (C) 20')[0]
                        except:
                            pass
                        try:
                            full_name = a[5]
                        except:
                            pass
                        try:
                            co_author = a[22]
                        except:
                            pass

                        try:
                            reprint_author = a[23].replace(' (reprint author)', '')
                        except:
                            pass
                        try:
                            title = a[8]
                        except:
                            pass
                        try:
                            keyword = a[20]
                        except:
                            pass
                        try:
                            author_keyword = a[19]
                        except:
                            pass
                        try:
                            abstract = a[21]
                        except:
                            pass
                        try:
                            citation = a[31]
                        except:
                            pass
                        try:
                            year = a[44]
                        except:
                            pass
                        try:
                            doi = a[54]
                        except:
                            pass
                        print(year,full_name, co_author, reprint_author, title, author_keyword, keyword, abstract,citation)
                        sv.save_DOI(year, full_name, co_author, reprint_author, title, author_keyword, keyword,
                                    abstract, citation, doi)
