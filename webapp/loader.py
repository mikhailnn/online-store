import csv
from webapp.db import db_session
from webapp.model import Catalog

def read_csv2(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['id', 'order_number', 'name', 'category_1', 'category_2', 'category_3', 
        'short_description', 'feature_1', 'feature_1_value', 'feature_1_measure_unit', 
        'made_in_country', 'producer_name', 'price', 'currency']
        reader = csv.DictReader(f, fields, delimiter=';')
        catalog_data = []
        for row in reader:
            catalog_data.append(row)
        save_catalog_data2(catalog_data)
        
def save_catalog_data2(catalog_data):
    db_session.bulk_insert_mappings(Catalog, catalog_data)
    db_session.commit()

if __name__ == '__main__':       
    read_csv2('price.csv')
    