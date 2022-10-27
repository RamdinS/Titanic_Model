import numpy as np
import json
import pickle
import config

class TitanicSurvival():
    def __init__(self,Pclass,Sex,Age,SibSp,Parch,Fare,Embarked):
        self.Pclass = Pclass
        self.Sex = Sex
        self.Age = Age
        self.SibSp = SibSp
        self.Parch = Parch
        self.Fare = Fare
        self.Embarked = Embarked

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.ENCODER_FILE_PATH,'r') as f:
            self.encoder = json.load(f)

    def predict(self):
        res=''
        self.load_model()
        self.Embarked = 'Embarked_' + self.Embarked

        test_array = np.zeros(len(self.encoder['columns']))
        test_array[0] = self.Pclass
        test_array[1] = self.encoder['sex'][self.Sex]
        test_array[2] = self.Age
        test_array[3] = self.SibSp
        test_array[4] = self.Parch
        test_array[5] = self.Fare
        test_array[self.encoder['columns'].index(self.Embarked)] = 1

        suvival = self.model.predict([test_array])

        if suvival == 0:
            res = 'Not Survived'
        else:
            res = 'Survived'
        
        return res