from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import Data_pre_processing as dataset

pipe_svc = make_pipeline(StandardScaler(), SVC(random_state=1))

param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]

param_grid = [{"svc_C": param_range, "svc_Kernel": ["linear"]},
              {"svc_C": param_range, "svc_gamma": param_range, "svc_kernel": ["rbf"]}]

gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring="accuracy",
                  cv=10, refit=True)

gs = gs.fit(X=dataset.X_train, y=dataset.y_train)

print("GS.best_score", gs.best_score_)

print("GS_best_parameter", gs.best_params_)
