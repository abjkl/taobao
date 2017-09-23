from flask import Flask,render_template,redirect,url_for,request,make_response
from database_setup import Base,Item,Shop,Sell_info
from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Create session and connect to DB
engine = create_engine('sqlite:////Users/gaoxinyi/Documents/GitHub/taobao/item.db',connect_args={'check_same_thread': False}, echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/',methods=['GET', 'POST'])
def all_item():
    items = session.query(Sell_info).filter(Sell_info.id==11376).filter_by(recom=None).all()
    if request.method == 'POST':
        ids = request.form['id']
        sell = session.query(Sell_info).filter_by(id = ids).one()
        sell.recom = 1
        session.add(sell)
        session.commit()
        n=int(ids)+1
        items = session.query(Sell_info).filter(Sell_info.id >= n,Sell_info.id<=n+200).filter_by(recom=None).all()
        return render_template('index.html', items=items)
    else:
        return render_template('index.html', items=items)


if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=8887)
