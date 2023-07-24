from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200))
    location = db.Column(db.String(100))
    payment_method = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean, default=False)

    favorites = db.relationship('Product', secondary='favorites')
    orders = db.relationship('Order', back_populates='user')

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            'id': self.id,
            'lastName': self.last_name,
            'firstName': self.first_name,
            'email': self.email,
            'address': self.address,
            'location': self.location,
            'paymentMethod': self.payment_method,
            'isAdmin': self.is_admin,
        }
    
class OrderItems(db.Model):
    __tablename__ = 'order_items'
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    product = db.relationship('Product', back_populates='orders')
    order = db.relationship('Order', back_populates='products')

    def serialize(self):
        return {
            'product': self.product.serialize(),
            'quantity': self.quantity
        }
    
class ProductSizesQuantity(db.Model):
    __tablename__= 'product_sizes_quantity'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    size_id = db.Column(db.Integer, db.ForeignKey('sizes.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)

    product = db.relationship("Product", back_populates="sizes_quantity")
    size = db.relationship("Size", back_populates="products")
    def serialize(self):
        return {
            "size": self.size.name,
            "quantity": self.quantity,
        }
    
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1000))
    color = db.Column(db.String(50))
    image_url = db.Column(db.String(200))
    type = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    category = db.relationship('Category', back_populates='products')
    orders = db.relationship('OrderItems', back_populates='product')
    sizes_quantity = db.relationship('ProductSizesQuantity', back_populates='product')        

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'color': self.color,
            'imageUrl': self.image_url,
            'type': self.type,
            "sizes_quantity": [size_quantity.serialize() for size_quantity in self.sizes_quantity]
        }
    
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50))

    user = db.relationship('User', back_populates='orders')
    products = db.relationship('OrderItems', back_populates='order')

    def serialize(self):
        return {
            'id': self.id,
            'user': self.user.serialize(),
            'orderDate': self.order_date,
            'status': self.status,
            'products': [p.serialize() for p in self.products]
        }
    
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    products = db.relationship('Product', back_populates='category')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
    
class Size(db.Model):
    __tablename__ = 'sizes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    products = db.relationship('ProductSizesQuantity', back_populates='size')
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

favorites = db.Table(
    'favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
)



    