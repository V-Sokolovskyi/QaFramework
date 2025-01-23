import pytest

@pytest.mark.databasealchemi
@pytest.mark.create_and_delete
def test1 (database_alchem):
    database_alchem.create_tabe(name_of_tabe="new12")
    
    if database_alchem.chek_table_exist("new12"):
        print("Table add to data")
    
    database_alchem.delete_table(name_of_table="new12")
    
    if database_alchem.chek_table_exist("new12") == False:
        print("Table delate from data")


@pytest.mark.databasealchemi
@pytest.mark.add_info
def test4(database_alchem_creat_delet_table):
    
    database_alchem_creat_delet_table.add_info('products_1')
    database_alchem_creat_delet_table.chek_added_info("products_1")



@pytest.mark.databasealchemi
@pytest.mark.update_info
def test3(database_alchem_creat_delet_table):
    
    database_alchem_creat_delet_table.add_info('products_1')
    database_alchem_creat_delet_table.update_info(name_of_table='products_1',)
    if database_alchem_creat_delet_table.chek_update_info(name_of_table= "products_1", new_name= "vasia") == True:
        print("Info update")
    else:
        print("Info not update")


# @pytest.mark.databasealchemi
# @pytest.mark.delete_base
def test2(database1):
    database1.delete_table(name_of_table="products_1")