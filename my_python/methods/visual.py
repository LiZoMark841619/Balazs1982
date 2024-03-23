import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from itertools import product as prod

def unique_and_fill(features: list, df: pd.DataFrame) -> any:
    for feature in features:
        if df[feature].dtype not in ['int64', 'float64']:
            df[feature] = df[feature].fillna('unknown')
        yield feature, df[feature].unique()

def change_values(new_values: list, df: pd.DataFrame, feature: str) -> pd.DataFrame:
    for value, element in prod(new_values, df[feature].unique()):
        if value in element:
            df[feature] = df[feature].replace(element, value)
    return df[feature]

def list_replacement(df: pd.DataFrame, feature: str, old_values: list, new_values: list) -> pd.DataFrame:
    for i in range(len(old_values)):
        df[feature] = df[feature].replace(old_values[i], new_values[i])
    return df[feature]

def pie_and_countplot(features: list, dataframe: pd.DataFrame) -> plt:
    for feat in features:
        data = dataframe[feat]
        if data.dtype == 'object':
            plt.figure(figsize=[10, 7])
            sns.set_palette('dark')
            plt.title(f'Distribution of {feat} of {len(data)} participants', fontsize = 16)
            if data.nunique() < 5:
                plt.pie(data.value_counts(), autopct='%d%%', pctdistance=0.85, explode=[0.035 for _ in range(data.nunique())], textprops={'color':'white'})
                plt.legend(data.unique(), loc='center')
                plt.gcf().gca().add_artist(plt.Circle((0, 0), 0.7, facecolor='white'))
            else:
                sns.countplot(y=feat, data=dataframe, saturation=0.75, hue='sex', order= dataframe[feat].value_counts().index)
                plt.xticks(rotation=15)
            plt.show()
    
def histogram(features:list, dataframe: pd.DataFrame) -> plt:
    for feat in features:
        data = dataframe[feat]
        if data.dtype in ['int64', 'float64']:
            plt.figure(figsize=[10, 7])
            sns.set_palette('dark')
            plt.title(f'Distribution of {feat} of {len(data)} participants', fontsize=16)
            sns.histplot(x=feat, data=dataframe, hue='sex', bins=30)
            mean = np.mean(data).round()
            plt.axvline(mean, color='red')
            plt.text(x=mean*1.1, y=7000, s=f'Mean: {mean}')
            plt.show()


def randfor_test_plot(depth, train_accu, test_accu):
    plt.plot(depth, train_accu, 'r-o', depth, test_accu, 'b-*')
    plt.title('Accuracy of training and test data')
    plt.xlabel('depth')
    plt.ylabel('accuracy')
    plt.legend(['training accuracy', 'test accuracy'])
    plt.show()
    plt.clf()
