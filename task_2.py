def get_cats_info(path):
    list_dic_cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                dict_cat_info = {}
                dict_cat_info['id'], dict_cat_info['name'], dict_cat_info['age'] = line.strip().split(',')
                # print(dict_cat_info)
                list_dic_cats.append(dict_cat_info)
        return list_dic_cats

    except Exception as e:
        print(f"Сталася помилка '{e}' під час читання файлу:")

cats_info = get_cats_info("cats_file.txt")
print(cats_info)