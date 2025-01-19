from sqlalchemy import create_engine,Column,Integer,String,Text,inspect
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base


class Database_alch():

    def __init__(self):
        #Conection to database 
        self.engine = create_engine('sqlite:///become_qa_auto.db', echo= False)
        
        #Automated get tables 
        self.Base = automap_base()
        self.Base.prepare(autoload_with=self.engine)
   

    def update_info(self,name_of_table):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        tabel_name = getattr(self.Base.classes, name_of_table)
        session.query(tabel_name).update({tabel_name.name:"vasia"})
        session.commit()
        session.close()

    
    def add_info(self,name_of_table):
        self.Base = automap_base()
        self.Base.prepare(autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        tabel_name = getattr(self.Base.classes, name_of_table)
        cost = 6
        Valute = 17
        
        new_record = tabel_name(name = "pepsi", description = "botel 0.85", Valut = Valute, cost = cost, total_cost = cost * Valute)
        session.add(new_record)
        session.commit()
        session.close()

    def chek_added_info(self,name_of_table):
        self.Base = automap_base()
        self.Base.prepare(autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        table_class = getattr(self.Base.classes, name_of_table)
        records = session.query(table_class).all()
        for record in records:
            print(f"Id:{record.id}," 
                  f"name:{record.name}," 
                  f"description:{record.description}," 
                  f"Valut:{record.Valut}," 
                  f"cost:{record.cost}," 
                  f"total_cost:{record.total_cost}"
                ) 
            print("Info added")  
        session.close()         
                  
    def chek_update_info(self, name_of_table, new_name):
        self.Base = automap_base()
        self.Base.prepare(autoload_with=self.engine)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        table_class = getattr(self.Base.classes, name_of_table)
        records = session.query(table_class).all()
        for record in records:
            record1 = record.name 
        return  record1 == new_name    
       
    
    
    def create_tabe(self, name_of_tabe):
        class New_tabel(self.Base):
            __tablename__ = name_of_tabe
            id = Column(Integer, primary_key=True)
            name = Column(Text)
            description = Column(Text)
            Valut = Column(Integer)
            cost = Column(Integer)
            total_cost = Column(Integer)
            
    
        self.Base.metadata.create_all(self.engine)

    def chek_table_exist(self, name_of_table):
        inspector = inspect(self.engine)
        tables = inspector.get_table_names()
        return name_of_table in tables
     

    def delete_table(self,name_of_table):
        self.Base = automap_base()
        self.Base.prepare(autoload_with=self.engine)
        table_class = getattr(self.Base.classes, name_of_table)
        table_class.__table__.drop(self.engine)


    









#For futer tests:


# with engine.connect() as connection:
#     connection.execute(text("ALTER TABLE test_table ADD COLUMN email TEXT"))
# New_data = Base.classes.test_table

