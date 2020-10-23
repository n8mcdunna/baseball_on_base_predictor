from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = dcc.Markdown("""
#### Data \n
The data used to build the model was from the 2015 through 2019 MLB baseball seasons. To reduce the size of the data to improve modeling runtimes the batters were sorted by their number of at bats. Then the data was filtered so that only the top fifty batters remained. The data was downloaded from kaggle(https://www.kaggle.com/pschale/mlb-pitch-data-20152018).

#### Baseline 63.908% \n
The target for predicting was the result of the at bat. This was created by assigning each baseball play like a strikeout, popout, single, home run, or error to either being on base or out.
For the data, batters were out 64.59% of at bats. Therefore for this binary classification prediction the baseline for measuring the models was this percentage. For this dataset there was a lot of leakage that had to be eliminated such as final game scores and number of outs.

#### Fitting a linear model 64.0159%
Using logistic regression the model barely beat the baseline with a cross validation accuracy score of 64.01%. As you can see by the graph below very few features had any impact on the accuracy. If a feature did have an impact the impact was very small and also negatively impacted the model.

![logistic regression permutation importances](/assets/log_reg_perm_imp.png)


#### Fitting a random forest model 58.14%
Using random forest classification the model severely underperformed with a cross validation accuracy score of 58.14%.

#### Fitting a XG Boost model 64.0149%
Using XGBoost the model scored 64.019, barely beating the baseline. Below you can see how each feature impacted the model.

![xgboost feature importances](assets/xg_feat_imp.png)

Here is a different method of looking at the importance of the features.

![xgboost permutation importances](/assets/xg_perm_imp.png)

The confusion matrix below for the XGBoost model shows that the accuracy barely beats the baseline because the model almost always chooses the runner as out.

![xgboost confusion matrix](/assets/xgb_confusion_matrix.png)

#### Final testing 63.439%
Since the logistic regression model performed the best that model was chosen to run the testing data on. For the testing data the accuracy score was 63.439.
""")

