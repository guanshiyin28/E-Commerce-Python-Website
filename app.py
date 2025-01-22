from flask import Flask, render_template
import requests as req
from models.product import Product 
import app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def kategori():
    return render_template("about.html")

@app.route('/product')
def produk():
    products=[]
    r=req.get('https://fakestoreapi.com/products')
    for product in r.json():
        products.append(
            Product(
                id=product['id'],
                title=product['title'],
                price=product['price'],
                description=product['description'],
                category=product['category'],
                image=product['image']
            )
        )
    return render_template("product.html", products=products)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):

    r=req.get(f'https://fakestoreapi.com/products/{product_id}')
    product=r.json()
    return render_template('detail_produk.html',product=product)

if __name__ == '__main__':
    app.run(debug=True)


