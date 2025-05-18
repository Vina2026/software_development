from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from sqlalchemy.sql import func



app = Flask(__name__)
app.secret_key = '12345'  #  secret key for flash messages and sessions


# Connecting to PostgreSQL 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:semsem123@localhost/COG'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Define user sign up model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)   #Hashes and stores the user's password safely

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  #Verifies entered password matches stored hash.


# Define donate form model
class donate_form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    item_name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    condition = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(150), nullable=False)
    delivery_method = db.Column(db.String(50), nullable=False)
    availability = db.Column(db.Text, nullable=True)
    additional_notes = db.Column(db.Text, nullable=True)
    anonymous = db.Column(db.Boolean, default=False)
    newsletter = db.Column(db.Boolean, default=False)



# New model for donated items available for request
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(100), nullable=False)
    condition = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    image_path = db.Column(db.String(200), nullable=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    available = db.Column(db.Boolean, default=True)


# Define request form model
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    item_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    delivery_method = db.Column(db.String(20), nullable=False)




# New model for cart functionality
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())


def get_featured_items(limit=6):
    return Item.query.filter_by(available=True).order_by(func.random()).limit(limit).all()


@app.route('/')
def index():
    items = get_featured_items(6)
    return render_template('index.html', items=items)


@app.route('/donate')
def donate():
    return render_template('donate.html')


@app.route('/request', methods=['GET'])
def request_donation():
    return render_template('request.html')





@app.route('/item-details/<int:item_id>')
def item_details(item_id):
    item = Item.query.get_or_404(item_id)
    return render_template('item-details.html', item=item)


@app.route('/cart')
def view_cart():
    if 'user_id' not in session:
        flash('Please log in to view your cart')
        return redirect(url_for('login'))
    
    cart_items = db.session.query(Item, Cart).join(Cart).filter(Cart.user_id == session['user_id']).all()
    return render_template('cart.html', cart_items=cart_items)


@app.route('/add-to-cart/<int:item_id>')
def add_to_cart(item_id):
    if 'user_id' not in session:
        flash('Please log in to add items to your cart')
        return redirect(url_for('login'))
    
    # Check if item already in cart
    existing = Cart.query.filter_by(user_id=session['user_id'], item_id=item_id).first()
    if existing:
        flash('Item already in cart')
        return redirect(url_for('view_cart'))
    
    # Add to cart
    cart_item = Cart(user_id=session['user_id'], item_id=item_id)
    db.session.add(cart_item)
    db.session.commit()
    flash('Item added to cart')
    return redirect(url_for('view_cart'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            flash('Email already registered.')
            return redirect(url_for('signup'))

        new_user = User(name=name, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')  # For GET requests


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash('Login successful!')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password.')
            return redirect(url_for('login'))

    return render_template('login.html')  # For GET requests


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('index'))


@app.route('/submit-donation', methods=['POST'])
def submit_donation():
    # Get form data with defaults
    anonymous = 'anonymous' in request.form
    newsletter = 'newsletter' in request.form

    donation = donate_form(
        first_name=request.form['firstName'],
        last_name=request.form['lastName'],
        email=request.form['email'],
        phone=request.form.get('phone', ''),
        item_name=request.form['itemName'],
        category=request.form['category'],
        condition=request.form['condition'],
        description=request.form['description'],
        location=request.form['location'],
        delivery_method=request.form['deliveryMethod'],
        availability=request.form.get('availability', ''),
        additional_notes=request.form.get('additionalNotes', ''),
        anonymous=anonymous,
        newsletter=newsletter
    )

    db.session.add(donation)
    db.session.commit()
    flash('Thank you for your donation!')

    return redirect(url_for('index'))




@app.route('/submit-request', methods=['POST'])
def submit_request():
    if 'user_id' not in session:
        flash('Please log in to request items.')
        return redirect(url_for('login'))

    new_request = Request(
        first_name=request.form['firstName'],
        last_name=request.form['lastName'],
        email=request.form['email'],
        phone=request.form.get('phone'),
        item_name=request.form['itemName'],
        category=request.form['category'],
        condition=request.form['condition'],
        description=request.form['description'],
        delivery_method=request.form['deliveryMethod']
    )

    db.session.add(new_request)
    db.session.commit()

    flash('Your request has been submitted!')
    return redirect(url_for('index'))



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# to delete item 
@app.route('/delete-item/<int:item_id>', methods=['POST', 'GET'])
def delete_item(item_id):
    if 'user_id' not in session:
        flash('Please log in to delete items')
        return redirect(url_for('login'))
    
    # Get the item
    item = Item.query.get_or_404(item_id)
    
    # Check if user is authorized (either the donor or implement admin check)
    if item.donor_id and item.donor_id != session['user_id']:
        flash('You are not authorized to delete this item')
        return redirect(url_for('available_items'))
    
    # Find related donation form entries
    donations = donate_form.query.filter_by(item_name=item.name).all()
    for donation in donations:
        db.session.delete(donation)
    
    # Delete any cart entries for this item
    cart_items = Cart.query.filter_by(item_id=item_id).all()
    for cart_item in cart_items:
        db.session.delete(cart_item)
    
    db.session.delete(item)
    db.session.commit()
    
    flash('Item has been deleted successfully')
    return redirect(url_for('available_items'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)