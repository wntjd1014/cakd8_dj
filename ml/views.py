from django.shortcuts import render
import joblib
import pandas as pd
import pickle

def inputdata(request):
    return render(request, 'ml/inputdata.html')

def ml_result(request):
    cls = joblib.load('ml/tcl_model.pkl')

    df = pd.DataFrame(columns=[['fare_cat', 'age_cat', 'family', 'female', 'male',
       'town_C', 'town_Q', 'town_S']]) 

    lis = []
    # one-hot encoding
    lis.append(request.GET['fare_cat'])
    lis.append(request.GET['age_cat'])
    lis.append(request.GET['family'])
    lis.append(request.GET['female'])
    lis.append(request.GET['male'])
    lis.append(request.GET['town_C'])
    lis.append(request.GET['town_Q'])
    lis.append(request.GET['town_S'])

    df.loc[0,:] = lis
    ans = cls.predict(df)
    if ans==0:
        ans = 'Dead'
    else:
        ans = 'Survived'
    return render(request, "ml/ml_result.html", {'lis':lis, 'ans':ans})

    