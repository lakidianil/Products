from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Prices per liter
milk_prices = {
    'buffalo': 80,
    'cow': 100
}

# Route to render the order page
@app.route('/')
def PRO_H():
    return render_template('index.html')

# Route to handle the order
@app.route('/order', methods=['POST'])
def order():
    # Retrieve form data from the order form
    name = request.form.get('name')
    address = request.form.get('address')
    number = request.form.get('number')
    product = request.form.get('product')
    quantity = request.form.get('quantity')


    # Validation
    if not name or not address or not number or not product or not quantity:
        return "All fields are required!", 400

    try:
        quantity = int(quantity)
    except ValueError:
        return "Quantity must be a valid number!", 400

    if product not in milk_prices:
        return "Invalid product selected!", 400

    total_amount = milk_prices[product] * quantity

    # Render confirmation page with the order details
    return render_template('index (2).html',
                           name=name,
                           address=address,
                           phone=number,
                           milk_type=product.capitalize(),
                           liters=quantity,
                           total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=True)
