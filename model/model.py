from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from model.preprocess import load_data
from model.preprocess import load_data

data = load_data()

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["symptoms"])

y = data["department"]

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, y)

def predict(symptom):
    symptom = symptom.lower()
    input_data = vectorizer.transform([symptom])
    return model.predict(input_data)[0]