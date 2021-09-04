import pickle

with open('emotions.pkl','rb') as f:
    a=pickle.load(f)
print(len(a))