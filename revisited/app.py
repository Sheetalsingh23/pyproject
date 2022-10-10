# from datetime import datetime
from flask import Flask ,render_template
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class ToDo(db.Model):
#     SrNo  = db.Column(db.Integer , primary_key = True)
#     title = db.Column(db.String(50) , nullable = False)
#     desc = db.Column(db.String(250) , nullable = False)
#     date_created = db.Column(db.DateTime , default = datetime.utcnow)


#     def __repr__(self) -> str:
#         return f"{self.SrNo} - {self.title}"

@app.route('/')
def hello():
    return "hekhfkl;dllo "
#     TOdo = ToDo(title = "first task" , desc="hjhkfdjhgkhfjhii just do it vro")
#     db.session.add(TOdo)
#     db.session.commit()
#     showTOdo = ToDo.query.all()
#     print(showTOdo)
#     return render_template('index.html' , showTOdo = showTOdo)
#     # return "hello world and dhiraj , how are you!"

# @app.route('/show')
# def show():
#     showTOdo = ToDo.query.all()
#     print(showTOdo)
#     return "done"

    
if __name__ == "__main__":
    app.run(debug= True , port=8000 )