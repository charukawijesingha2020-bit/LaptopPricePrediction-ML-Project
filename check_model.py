import pickle

model = pickle.load(open("laptop_price_model_final.pkl", "rb"))

print(type(model))

try:
    print("Features:", model.n_features_in_)
except:
    print("No feature count")

try:
    print(model.feature_names_in_)
except Exception as e:
    print("No feature names")
    print(e)