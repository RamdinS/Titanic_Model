from flask import Flask,jsonify,request
import config
from project_app.utils import TitanicSurvival

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HOME PAGE"

@app.route('/predict')
def predict():
    input = request.get_json()
    Pclass = input['Pclass']
    Sex = input['Sex']
    Age = input['Age']
    SibSp = input['SibSp']
    Parch = input['Parch']
    Fare = input['Fare']
    Embarked = input['Embarked']

    titanic = TitanicSurvival(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked)
    output = titanic.predict()

    return jsonify({'Result':f'The person did {output}'})

if __name__ == '__main__':
    app.run(host=config.HOST_NAME,port=config.PORT_NO,debug=True)