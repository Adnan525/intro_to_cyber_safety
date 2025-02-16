from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Shopping Cart Demo</title>
</head>
<body>
    <h1>🛒 Persistent Shopping Cart</h1>

    <h3>Items in Cart:</h3>
    <ul>
        {% for item in cart %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>

    <form action="/" method="POST">
        <label for="item">Add an item:</label>
        <input type="text" name="item" required>
        <input type="submit" value="Add to Cart">
    </form>

    <a href="/delete_cookie"><button>🗑 Clear Cookies</button></a>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def shopping_cart():
    cart = request.cookies.get('cart')
    cart_items = cart.split(',') if cart else []

    if request.method == 'POST':  # Adding item to cart
        new_item = request.form.get('item')
        cart_items.append(new_item)

    response = make_response(render_template_string(HTML_TEMPLATE, cart=cart_items))
    response.set_cookie('cart', ','.join(cart_items), max_age=60 * 5)  # Store cart in a cookie (5 min)
    return response


@app.route('/delete_cookie')
def delete_cookie():
    response = make_response("<p>Cart reset! <a href='/'>Go back</a></p>")
    response.delete_cookie('cart')
    return response


if __name__ == '__main__':
    app.run(debug=True)
