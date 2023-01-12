
import pickle
model = pickle.load(open('SFBN.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))

new_email = "Hi this is Steve"
new_features = cv.transform([new_email])
prediction = model.predict(new_features)
if prediction[0]==1:
    print ("Spam Detected")
else:
    print ("Ham Detected")

    