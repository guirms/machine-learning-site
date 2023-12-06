import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import re

dataframe = pd.read_csv('data.csv', index_col=False)
dataframe.drop(['id', "Unnamed: 32"], axis=1, inplace=True)

scaler_radius_mean = MinMaxScaler()
dataframe['radius_mean'] = scaler_radius_mean.fit_transform(dataframe['radius_mean'].values.reshape(-1, 1))

scaler_texture_mean = MinMaxScaler()
dataframe['texture_mean'] = scaler_texture_mean.fit_transform(dataframe['texture_mean'].values.reshape(-1, 1))

scaler_perimeter_mean = MinMaxScaler()
dataframe['perimeter_mean'] = scaler_perimeter_mean.fit_transform(dataframe['perimeter_mean'].values.reshape(-1, 1))

scaler_area_mean = MinMaxScaler()
dataframe['area_mean'] = scaler_area_mean.fit_transform(dataframe['area_mean'].values.reshape(-1, 1))

scaler_radius_se = MinMaxScaler()
dataframe['radius_se'] = scaler_radius_se.fit_transform(dataframe['radius_se'].values.reshape(-1, 1))

scaler_texture_se = MinMaxScaler()
dataframe['texture_se'] = scaler_texture_se.fit_transform(dataframe['texture_se'].values.reshape(-1, 1))

scaler_perimeter_se = MinMaxScaler()
dataframe['perimeter_se'] = scaler_perimeter_se.fit_transform(dataframe['perimeter_se'].values.reshape(-1, 1))

scaler_area_se = MinMaxScaler()
dataframe['area_se'] = scaler_area_se.fit_transform(dataframe['area_se'].values.reshape(-1, 1))

scaler_radius_worst = MinMaxScaler()
dataframe['radius_worst'] = scaler_radius_worst.fit_transform(dataframe['radius_worst'].values.reshape(-1, 1))

scaler_texture_worst = MinMaxScaler()
dataframe['texture_worst'] = scaler_texture_worst.fit_transform(dataframe['texture_worst'].values.reshape(-1, 1))

scaler_perimeter_worst = MinMaxScaler()
dataframe['perimeter_worst'] = scaler_perimeter_worst.fit_transform(dataframe['perimeter_worst'].values.reshape(-1, 1))

scaler_area_worst = MinMaxScaler()
dataframe['area_worst'] = scaler_area_worst.fit_transform(dataframe['area_worst'].values.reshape(-1, 1))

x = dataframe.drop('diagnosis', axis=1)
y = dataframe['diagnosis']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

dataframe['diagnosis'].value_counts().plot(kind='bar',edgecolor='black',color=['lightsteelblue','navajowhite'])

svc_model = {
    'name': 'SVC',
    'model': SVC(),
    'params': {
        "gamma": [0.001, 0.01, 0.1, 1],
        'C': [1, 10, 50, 100, 200, 300, 1000],
        'kernel': ['rbf'],
    }
}

knn_model = {
    'name': 'KNeighborsClassifier',
    'model': KNeighborsClassifier(),
    'params': {
        'n_neighbors': [2, 3, 5, 7, 9],
        'weights': ['uniform', 'distance'],
        "metric": ["euclidean", "manhattan"]
    }
}

decision_tree_model = {
    'name': 'DecisionTreeClassifier',
    'model': DecisionTreeClassifier(),
    'params': {'criterion': ['gini', 'entropy'],
          'splitter': ['best', 'random'],
          'min_samples_split': [2,5,10],
          'min_samples_leaf': [1,5,10]}
}

desired_metric = 'accuracy'

def train_and_evaluate_model(model_info, x_train, y_train, x_test, y_test):
    grid_search = GridSearchCV(model_info['model'], model_info['params'], cv=5, n_jobs=-1, scoring=desired_metric)
    grid_search.fit(x_train, y_train)

    best_model_info = {
        'name': model_info['name'],
        'best_model': grid_search.best_estimator_,
        'best_params': grid_search.best_params_,
        'best_score': grid_search.best_score_
    }

    y_pred = grid_search.predict(x_test)
    classification_rep = classification_report(y_test, y_pred)
    best_model_info['classification_report'] = classification_rep

    return best_model_info


def print_results(result):
    print(f"\nModelo: {result['name']}")
    print(f"Melhores parâmetros: {result['best_params']}")
    print(f"Melhor {desired_metric.capitalize()}: {round(result['best_score'] * 100, 2)}%")
    print("Relatório de classificação:")
    print(result['classification_report'])

def clean_text(text):
    breakline_index = text.find("\n")

    if breakline_index != -1:
        text = text[breakline_index + 1:]

    return text
    

def get_predict():
    svc_result = train_and_evaluate_model(svc_model, x_train, y_train, x_test, y_test)
    knn_result = train_and_evaluate_model(knn_model, x_train, y_train, x_test, y_test)
    decision_tree_result = train_and_evaluate_model(decision_tree_model, x_train, y_train, x_test, y_test)

    results = [svc_result, knn_result, decision_tree_result]
    list_to_return = []

    for result in results:
        list_to_return.append(return_results(result))

    return list_to_return

def return_results(result):
    clean_classification_report = clean_text(result['classification_report'])
    clean_classification_values = re.findall(r'\d+\.\d+|\d+', clean_classification_report)
    clean_classification_values = [float(numero) for numero in clean_classification_values]

    precision = {
        'b': clean_classification_values[0],
        'm': clean_classification_values[4],
        'accuracy': '',
        'macro_avg': clean_classification_values[10],
        'weighte_avg': clean_classification_values[14]
    }

    recall = {
        'b': clean_classification_values[1],
        'm': clean_classification_values[5],
        'accuracy': '',
        'macro_avg': clean_classification_values[11],
        'weighte_avg': clean_classification_values[15]
    }

    f1_score = {
        'b': clean_classification_values[2],
        'm': clean_classification_values[6],
        'accuracy': clean_classification_values[8],
        'macro_avg': clean_classification_values[12],
        'weighte_avg': clean_classification_values[16]
    }

    support = {
        'b': clean_classification_values[3],
        'm': clean_classification_values[7],
        'accuracy': clean_classification_values[9],
        'macro_avg': clean_classification_values[13],
        'weighte_avg': clean_classification_values[17]
    }
    
    return {
        'model': result['name'],
        'best_params': result['best_params'],
        'best_accuracy': round(result['best_score'] * 100, 2),
        'classification_report': {
            'precision': precision,
            'recall': recall,
            'f1_score': f1_score,
            'support': support
        }
    }
    

# svc_result = train_and_evaluate_model(svc_model, x_train, y_train, x_test, y_test)
# knn_result = train_and_evaluate_model(knn_model, x_train, y_train, x_test, y_test)
# decision_tree_result = train_and_evaluate_model(decision_tree_model, x_train, y_train, x_test, y_test)

# results = [svc_result, knn_result, decision_tree_result]

# for result in results:
#     print_results(result)



