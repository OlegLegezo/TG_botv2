from loader import db

print(db.select_all_users())
# print(db.select_user_info(id=661888342))
# print(db.update_user_phone(id=262086056,phone='987654321'))
# print(db.delete_user(id=661888342))
# print(db.select_all_users())


import db_api

db = db_api.Database('db_api/database/shop_database.db')
# db.add_item(id=1, name='Огурцы', count=30, photo_path=r'db_api/database/product_photo/cucumber.jpeg')
# db.add_item(id=2, name='Картофель', count=31, photo_path=r'db_api/database/product_photo/potato.jpeg')
# db.add_item(id=3, name='Помидоры', count=32, photo_path=r'db_api/database/product_photo/tomato.jpeg')
# db.add_item(id=4, name='Кабачки', count=33, photo_path=r'db_api/database/product_photo/zucchini.jpeg')
print(db.select_all_items())
print(db.get_items_count())
# db.delete_all()