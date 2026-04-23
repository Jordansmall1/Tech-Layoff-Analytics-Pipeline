import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
engine = create_engine('postgresql://postgres:postgres@localhost:5432/layoff_pipeline')

df = pd.read_sql('SELECT * FROM core.layoffs', engine)
print(df.shape)
print(df.head())

df['layoff_risk'] = (df['percentage_laid_off'] > 0.15).astype(int)
print(df['layoff_risk'].value_counts())
#0-2897#
#1-1460#

features = ['industry', 'country', 'stage', 'funds_raised']
df_model = df[features + ['layoff_risk']].dropna()
print(df_model.shape)

X = pd.get_dummies(df_model[features])
y = df_model['layoff_risk']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_pred, y_test))
print('AUC:', roc_auc_score(y_test, model.predict_proba(X_test)[:,1]))
importance = pd.DataFrame({ 'feature': X.columns, 'importance': model.feature_importances_
}).sort_values('importance', ascending=False)
print(importance.head(10))