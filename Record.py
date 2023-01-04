
class record:
    def __init__(self, year_='', authorList_='', authorInstitute_='', reprintAuthor_='', title_='', citation_='',
                 pubmed_id_=''):
        self.authorInstitute = authorInstitute_
        self.authorList = authorList_
        self.authorName_order_dict = {}
        self.author_name_set = set()
        self.author_number = 0
        self.author__institute_list__dict = {}  ###self.author__institute_set__dict[author_name]= []
        self.citation = citation_
        self.first_author = ''
        self.institute_country_order_dict = {}
        self.institute_country_set = set()
        self.pubmed_id = pubmed_id_
        self.reprintAuthor = reprintAuthor_
        self.reprint_author_set = set()
        self.title = title_
        self.year = year_

    def set_authorInstitute(self, authorInstitute_):
        self.authorInstitute = authorInstitute_

    def set_authorList(self, authorList_):
        self.authorList = authorList_

    def set_authorName_order(self, author_name, order):
        self.authorName_order_dict[author_name] = order

    def add_author_name_set(self, author_name):
        self.author_name_set.add(author_name)

    def add__author_institute_list__map(self, author_name, ins_cou):
        if author_name not in self.author__institute_list__dict:
            self.author__institute_list__dict[author_name] = []
        if ins_cou not in self.author__institute_list__dict[author_name]:
            self.author__institute_list__dict[author_name].append(ins_cou)

    def set_citation(self, citation_):
        self.citation = citation_

    def set_first_author(self, author_):
        self.first_author = author_

    def set_institute_country_order(self, ins_cou, order):
        self.institute_country_order_dict[ins_cou] = order

    def add_institute_country_set(self, ins_cou):
        self.institute_country_set.add(ins_cou)

    def set_pubmed_id(self, pubmed_id_):
        self.pubmed_id = pubmed_id_

    def set_reprintAuthor(self, repriintAuthor_):
        self.reprintAuthor = repriintAuthor_

    def add_reprint_author_set(self, author):
        self.reprint_author_set.add(author)

    def set_title(self, title_):
        self.title = title_

    def set_year(self, year_):
        self.year = year_

    ############################################################################
    def get_authorInstitute(self):
        return self.authorInstitute

    def get_authorList(self):
        return self.authorList

    def get_author_name_set(self):
        return self.author_name_set

    def get_author_number(self):
        self.author_number = len(self.author_name_set)
        return self.author_number

    def get_authorName_order_dict(self):
        return self.authorName_order_dict

    def get__author_institute_list__map(self):
        return self.author__institute_list__dict

    def get_citation(self):
        return self.citation

    def get_first_author(self):
        return self.first_author

    def get_init(self):
        return self.year, self.title, self.authorList, self.authorInstitute, self.reprintAuthor, self.citation, self.pubmed_id

    def get_institute_country_set(self):
        return self.institute_country_set

    def get_pubmed_id(self):
        return self.pubmed_id

    def get_reprintAuthor(self):
        return self.reprintAuthor

    def get_reprint_author_set(self):
        return self.reprint_author_set

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year