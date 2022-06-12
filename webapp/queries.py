from model import Catalog



def goods():
    catalogs = Catalog.query.order_by(Catalog.order_number).all()
    for g in catalogs:
        print(f'{g.name}')
    return catalogs

if __name__ == '__main__':
    goods()