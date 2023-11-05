"""
    model training
"""
import os
import sys
from dataclasses import dataclass
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


# current_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(current_dir)
# sys.path.append(parent_dir)
# from exception import CustomException
# from logger import logging
# from utils import save_object, evaluate_model

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_model


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("../../artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")

            x_train, y_train, x_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            print("trainTest>>>", x_train, y_train)

            models = {
                "Logistics Classifier": LogisticRegression(
                    random_state=0, max_iter=200
                ),
                "kNN classifier ": KNeighborsClassifier(
                    n_neighbors=4, algorithm="ball_tree"
                ),
                "Random Forest classifier": RandomForestClassifier(
                    max_depth=2, random_state=0
                ),
                "AdaBoost Classifier": AdaBoostClassifier(
                    n_estimators=100, random_state=0
                ),
            }

            model_report: dict = evaluate_model(
                x_train=x_train,
                y_train=y_train,
                x_test=x_test,
                y_test=y_test,
                models=models,
                scoreMatrice=metrics,
            )

            print("modelReport>>>", model_report, model_report["testingPerformance"])

            best_model_score = max(sorted(model_report["testingPerformance"]))

            best_model_score_index = model_report["testingPerformance"].index(
                best_model_score
            )

            best_model_name = model_report["modelNames"][best_model_score_index]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info(
                f"best model {best_model_name} found with score {best_model_score}"
            )

            save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)

            logging.info(f"model pkl created")

            return best_model_score
        except Exception as e:
            raise CustomException(e, sys)
