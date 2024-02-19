from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False)
    menu_item = db.Column(db.String(80), nullable=False)

@app.route('/order', methods=['POST'])
def place_order():
    order = Order(table_number=request.json['table_number'], menu_item=request.json['menu_item'])
    db.session.add(order)
    db.session.commit()
    return {'id': order.id}

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
