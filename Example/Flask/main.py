from flask import Flask, jsonify, render_template
import requests


app = Flask(__name__)

@app.route('/') #decorator
def index():
  return render_template('index.html')

#routing: 사용자의 접속 경록 지정


#외부 api정보 가져오기

@app.route('/posts')
def show_posts():
  response = requests.get('https://jsonplaceholder.typicode.com/posts')
  to_serve = response.json()
  return jsonify(to_serve)

@app.route('/posts/<int:post_num>/comments')
def show_comments(post_num):
  response = requests.get('https://jsonplaceholder.typicode.com/posts/{}/comments'.format(post_num))
  to_serve = response.json()
  return jsonify(to_serve)

@app.route('/quote/<string:name>')
def show_quote(name=None):

  return "This is quote {}".format(name)

#rendering with template

# data
product_list = [
  {
    'product_id': 10000001,
    'product_name': 'shoes',
    'price': 12000,
    'currency': 'KRW',
  },
  {
    'product_id': 10000002,
    'product_name': 'cap',
    'price': 25.99,
    'currency': 'USD',
  },
]

# get all products
@app.route('/products')
def show_product_list():
  result= {'items':product_list}
  return render_template('products.html', items=result)

# get product detail
@app.route('/products/<int:product_id>')
def show_product(product_id=None):
  result = next(item for item in product_list if item['product_id'] == product_id)
  return render_template('product.html', item=result)

if __name__ =='__main__':
  app.run(host='0.0.0.0',port=4000, debug=True)
  