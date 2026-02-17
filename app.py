from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Inicio')


@app.route('/about')
def about():
    return render_template('about.html', title='Acerca de')


@app.route('/productos')
def productos():
    products = [
        {'id': 1, 'name': 'Producto A', 'price': 10.0},
        {'id': 2, 'name': 'Producto B', 'price': 20.0},
    ]
    return render_template('products.html', title='Productos', products=products)


@app.route('/clientes')
def clientes():
    clients = [
        {'id': 1, 'name': 'Cliente 1'},
        {'id': 2, 'name': 'Cliente 2'},
    ]
    return render_template('clients.html', title='Clientes', clients=clients)


@app.route('/facturas')
def facturas():
    invoices = [
        {'id': 1001, 'client': 'Cliente 1', 'total': 50.0},
    ]
    return render_template('invoices.html', title='Facturas', invoices=invoices)


if __name__ == '__main__':
    app.run(debug=True)
