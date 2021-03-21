from _functions.config import config
import psycopg2
import pandas as pd

"""
pseudocode for content filtering

1. Categorys gaan pakken
2. Orders/events pakken 
2a/ populaire producten pakken
2b/ genders pakken
2c/ prijzen pakken
2d/ brand pakken
2e/ product name pakken
2f/ variant pakken?
2g/ aanbieding pakken/folder actief
3. query analyseren
4. visitors en products aan linken in koppeltabel similars
5. recommendations geven

"""



class ContentRules:

    def __init__(self):
        pass

    def openconnection(self):
        db = config()
        con = psycopg2.connect(**db)
        return con

    def create_table(self, target):
        con = self.openconnection()
        cur = con.cursor()
        df = self.get_data_catagory()
        lst_names = df.columns
        query = f"CREATE TABLE {target} (idProducts VARCHAR(255) NOT NULL,  name VARCHAR(255) NULL,  brand VARCHAR(255) NULL,  category VARCHAR(255) NULL,);"


    def get_data_catagory(self, category):
        ''' haal de data catagory uit postgres '''
        con = self.openconnection()
        query = pd.read_sql_query(f"select idproducts, name, brand, category from products where category = '{category}' order by random() limit 10;", con)
        df = pd.DataFrame(query, columns=['idproducts','name','brand','category'])
        return df










    # def filter_lst(self, lst):
    #     new_lst = []
    #     for i in lst:
    #         word_list = list(i)
    #         for j in word_list:
    #             if j == '&':
    #                 x = i.replace('&', 'and')
    #                 new_lst.append(x)
    #             elif j == '-':
    #                 y = i.replace('-', ' ')
    #                 new_lst.append(y)
    #
    #
    #     print(new_lst)
    #     return new_lst
    #
    #
    #
    #

    #
    # def sort_data(self):
    #     ''' sorteer dezelfde elementen bij elkaar van de ontvangen data '''
    #     df = self.get_data_catagory()
    #     ids = list(df['idproducts'])
    #     catagorys = list(df['category'])
    #     unique_catagorys = list(df['category'].unique())
    #     lst = []
    #     for unique in unique_catagorys:
    #         lst1 = []
    #         for index, value in enumerate(catagorys):
    #             if unique == value:
    #                 id = ids[index]
    #                 category_id = (id, value)
    #                 lst1.append(category_id)
    #         lst.append(lst1)
    #
    #     return lst
    #
    # def make_table(self, name):
    #     ''' maak een nieuwe tabel aan met de data die je krijgt '''
    #     con = self.openconnection()
    #     cur = con.cursor()
    #     data = self.sort_data()
    #     df = self.get_data_catagory()
    #     unique_catagorys = list(df['category'].unique())
    #     print(unique_catagorys)
    #     print(self.filter_lst(lst=unique_catagorys))
    #     make_table_query = f"CREATE TABLE IF NOT EXISTS {name}();"
    #     cur.execute(make_table_query)
    #     lst = []
    #     for i in unique_catagorys:
    #         query = f"ADD COLUMN {i} INT constraint;"
    #         lst.append(query)
    #
    #
    #
    #
    #
