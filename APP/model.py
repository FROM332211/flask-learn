from APP.ext import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(16), nullable=False)

    def save(self):  # 添加数据
        db.session.add(self)
        db.session.commit()


class commodity_base_info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commodity_type = db.Column(db.String(30), nullable=False)
    commodity_name = db.Column(db.String(30), nullable=False)
    commodity_brand = db.Column(db.String(30), nullable=False)
    commodity_base_price = db.Column(db.String(30), nullable=False)
    img_path = db.Column(db.String(30), nullable=False)
    info = db.Column(db.String, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()


class commodity_price_info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commodity_type = db.Column(db.String(30), nullable=False)
    commodity_name = db.Column(db.String(30), nullable=False)
    commodity_brand = db.Column(db.String(30), nullable=False)
    price = db.Column(db.String(30), nullable=False)
    price_url = db.Column(db.String, nullable=False)
    price_title = db.Column(db.String, nullable=False)
    price_img_path = db.Column(db.String(30), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()


class commodity_review_info(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commodity_type = db.Column(db.String(30), nullable=False)
    commodity_name = db.Column(db.String(30), nullable=False)
    commodity_brand = db.Column(db.String(30), nullable=False)
    review_url = db.Column(db.String(30), nullable=False)
    review_title = db.Column(db.String, nullable=False)
    review_img_path = db.Column(db.String, nullable=False)
    review_excerpt = db.Column(db.String, nullable=False)

    # zhihu_x_zse_86 = db.Column(db.String, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()


class user_collection(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=True)
    commodity_info_id = db.Column(db.Integer, nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self, row):
        db.session.delete(row)
        db.session.commit()


class commodity_history_price(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commodity_price_id = db.Column(db.Integer, nullable=True)
    insert_time = db.Column(db.DATETIME, nullable=True)
    price = db.Column(db.String(30), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def save_all(self, price_list):
        price = []
        for i in price_list:
            price.append(commodity_history_price(commodity_price_id=i[0], price=i[1], insert_time=i[2]))
        db.session.add_all(price)
        db.session.commit()
