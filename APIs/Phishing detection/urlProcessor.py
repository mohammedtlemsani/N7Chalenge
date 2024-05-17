import pickle
import numpy as np
import pandas as pd
from Features import FeatureExtraction

# Load the trained model
with open('resources/phishingModel.pkl', 'rb') as file:
    phishing_model = pickle.load(file)



# Prediction function
def predict(url):
    features = FeatureExtraction(url).getFeaturesList()

    # Convert features to DataFrame with the correct column names
    feature_df = pd.DataFrame([features])
    return phishing_model.predict(feature_df)

# Example URL
# url = "www.google.com"


with open('resources/nlp.pkl', 'rb') as file:
    nlp = pickle.load(file)

def predictNlp(text):
    return nlp.predict(text)

# Predict
# prediction = predict(url)
# map = {
#     -1:True,
#     1:False
# }



# print(prediction)
# print(predictNlp("Dear Valued Customer,We have detected unusual activity on your account and, as a precaution, we have temporarily suspended access to your account. To ensure that your account remains secure, please verify your information by clicking the link below within the next 24 hours:Verify Your AccountFailure to verify your account will result in permanent suspension and loss of access to your funds. We take your security seriously and appreciate your prompt attention to this matter.If you did not attempt to log in from an unfamiliar location, please contact our support team immediately.Thank you for your cooperation.Best regards,"))
