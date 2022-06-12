from sqlalchemy import Column, Integer, Float, String
from webapp.db import Base, engine


class Catalog(Base):
    __tablename__ = "goods"

    id = Column(Integer, primary_key=True)
    order_number = Column(Integer)
    name = Column(String)  
    category_1 = Column(String)
    category_2 = Column(String)
    category_3 = Column(String)
    short_description = Column(String)
    feature_1 = Column(String)
    feature_1_value = Column(Float)
    feature_1_measure_unit = Column(String)  
    made_in_country = Column(String)
    producer_name = Column(String)
    price = Column(Float)
    currency = Column(String)

    def __repr__(self):
        return (f"{self.name}, {self.id}, \
                {self.short_description}, \
                {self.feature_1}, {self.feature_1_value}, {self.feature_1_measure_unit}, \
                {self.producer_name}, {self.made_in_country}, \
                {self.price}, {self.currency}")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)