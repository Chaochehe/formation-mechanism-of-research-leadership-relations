from KPL_Class import kpl

def Gen_weighted_list():
    title_idx_dict = kpl.kpl_save_read('..\\data_temp\\title_idx_dict').read()
    titleIdx_author_index = kpl.kpl_save_read(
        "..\data_temp\\titleIdx_author_index").read()  # {titleidx : {authorname: authorIdx}}
    Author_id = kpl.kpl_save_read(
        '..\data_temp\\Author_id').read()  # authorIdx authorInstitute dict
    title_parsed_record_dict = kpl.kpl_save_read('..\data_temp\\title_parsed_record_dict').read()

    Author_id1_author_id2_dict = kpl.kpl_save_read(
        '..\data_temp\\Author_id1_author_id2_dict').read()

    links_coauthor = {}

    links_lead_partici = {}

    for title in title_parsed_record_dict:
        this_record_instance = title_parsed_record_dict[title]
        titleIdx = title_idx_dict[title]
        leadingAuthorSet = set()
        firstAuthor = this_record_instance.get_first_author()
        first_AuthorId = titleIdx_author_index[titleIdx][firstAuthor]
        firstAuthor_disbgedIdx = Author_id1_author_id2_dict[first_AuthorId]
        if firstAuthor_disbgedIdx in Author_id:
            leadingAuthorSet.add(firstAuthor_disbgedIdx)
        reprint_set = this_record_instance.get_reprint_author_set()
        for reprint_name in reprint_set:
            reprintId = titleIdx_author_index[titleIdx][reprint_name]
            reprint_disbgedIdx = Author_id1_author_id2_dict[reprintId]
            if reprint_disbgedIdx in Author_id:
                leadingAuthorSet.add(reprint_disbgedIdx)

        author_set = this_record_instance.get_author_name_set()
        coauthorIdSet = set()
        for coauthor_name in author_set:
            coauthorId = titleIdx_author_index[titleIdx][coauthor_name]
            coauthor_disbgedIdx = Author_id1_author_id2_dict[coauthorId]
            if coauthor_disbgedIdx in Author_id:
                coauthorIdSet.add(coauthor_disbgedIdx)

        for disbgedIdx_i in coauthorIdSet:
            if disbgedIdx_i not in links_coauthor:
                links_coauthor[disbgedIdx_i] = {}

            for disbgedIdx_j in coauthorIdSet:
                if disbgedIdx_j != disbgedIdx_i:
                    if disbgedIdx_j not in links_coauthor[disbgedIdx_i]:
                        links_coauthor[disbgedIdx_i][disbgedIdx_j] = 0.0
                    links_coauthor[disbgedIdx_i][disbgedIdx_j] += 1.0

            if disbgedIdx_i not in links_lead_partici:
                links_lead_partici[disbgedIdx_i] = {}

            for leadingAuthor in leadingAuthorSet:
                if disbgedIdx_i != leadingAuthor:
                    if leadingAuthor not in links_lead_partici[disbgedIdx_i]:
                        links_lead_partici[disbgedIdx_i][leadingAuthor] = 0.0
                    links_lead_partici[disbgedIdx_i][leadingAuthor] += 1

    kpl.kpl_save_read('data_temp\\links_coauthor').save(links_coauthor)
    kpl.kpl_save_read('data_temp\\links_lead_partici').save(links_lead_partici)
