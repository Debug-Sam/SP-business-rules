import os
import time

from _functions.setup_database import create_database, fill_database, drop_database
from classes.poducts_filter import FilterProducts
from classes.pymongo_converter import Converter
from classes.send_data import DataSender
from classes.sessions_filter import FilterSessions
from Rules.Content_rules import ContentRules

'''
Create converter and select the wanted fieldnames.
Also give the name of the file u want to create.
'''

# Create and fill the database with the table structure
# drop_database()
# create_database()
# fill_database()
#
# converter = Converter()
# converter.products(fieldnames=['_id', 'name', 'brand', 'category', 'deeplink', 'properties.doelgroep', 'fast_mover', 'gender', 'herhaalaankopen', 'price.selling_price'], filename='products.csv')
#
# '''
# Create filter and load in the file. then replace the wanted values.
#
# After that save the new data and print te amount of <null> values in the csv file to check if the filtering process worked.
# '''
#
# filter_products = FilterProducts()
# filter_products.load_dataframe(filename='products.csv')
# filter_products.replace_null(columns=['_id', 'name', 'brand', 'category', 'deeplink', 'fast_mover', 'gender', 'herhaalaankopen', 'selling_price', 'doelgroep'])
# filter_products.replace_doelgroep()
# filter_products.replace_gender(invalid=['Gezin', 'B2B', 'Kinderen', 'Senior', 'Baby', 'Grootverpakking', '8719497835768'])
# filter_products.save_dataframe()
# print(filter_products.dataframe.isna().sum())
#
# # Create sender and query the products
#
# absolutepath = os.getcwd()
#
# data_sender = DataSender()
# data_sender.copy_products_csv(pathname = absolutepath + "\products.csv")
#
# converter.visitors(fieldnames=['recommendations.segment', 'recommendations.latest_visit'], filename='visitors.csv')
#
# data_sender.copy_visitors_csv(pathname= absolutepath + "\visitors.csv")
#
# converter.sessions(fieldnames=['user_agent.identifier', 'session_start', 'session_end'], filename='sessions.csv')
#
# filter_sessions = FilterSessions()
# filter_sessions.load_dataframe(filename='sessions.csv')
# filter_sessions.save_dataframe()
#
# data_sender.copy_sessions_csv(pathname=absolutepath + "\sessions.csv")

content = ContentRules()
content.create_table(target='Gezond & verzorging', type='category')
content.create_table(target='Huishouden', type='category')
content.create_table(target='Elektronica & media', type='category')
content.create_table(target='Eten & drinken', type='category')
content.create_table(target='Make-up & geuren', type='category')
content.create_table(target='Baby & kind', type='category')
content.create_table(target='50% korting', type='category')
content.create_table(target='Nieuw', type='category')
content.create_table(target='Kleding & sieraden', type='category')
content.create_table(target='op=opruiming', type='category')
content.create_table(target='Cadeau ideeën', type='category')
content.create_table(target='Folder artikelen', type='category')
content.create_table(target='Black Friday', type='category')
content.create_table(target='Extra Deals', type='category')
content.create_table(target='Opruiming', type='category')
content.create_table(target='onbekend', type='category')

content.create_table(target='8x4', type='brand')



