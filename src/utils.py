# for common functions

import os
import sys
# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.append(parent_dir)
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException
# from src.exception import CustomException


def save_object(file_path, obj):
    try:
        print("filePath>>>", file_path)
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_model(x_train,y_train, x_test, y_test, models,scoreMatrice,GridSearchCV,hyperParams):
    try:
        report  ={}
        model_name=[]
        model_train_performance=[]
        model_test_performance=[]

        for i in range(len(list(models))):
            modelName=list(models.keys())[i]
            model_name.append(modelName)

            
            model = list(models.values())[i]
            
            tuningParams= list(hyperParams.values())[i]
            gs=GridSearchCV(model,tuningParams, cv=5)
            gs.fit(x_train,y_train)

            print("modelParams>>>",gs.best_params_)
            model.set_params(**gs.best_params_)
            model.fit(x_train,y_train)
            
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)
            
            train_accuracy=scoreMatrice.accuracy_score(y_train,y_train_pred)
            test_accuracy = scoreMatrice.accuracy_score(y_test,y_test_pred)

            model_train_performance.append(train_accuracy)
            model_test_performance.append(test_accuracy)

        report={'modelNames':model_name, 'trainingPerformance':model_train_performance,'testingPerformance':model_test_performance}
        print("report>>>", report)
        return report

        
    except Exception as e:
        raise CustomException(e,sys)