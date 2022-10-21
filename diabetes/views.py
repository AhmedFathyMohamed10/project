from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def make_prediction(request):
    
    if request.method == 'POST':
        # Get the data from the form
        pregnancies = request.POST.get('pregnancies')
        glucose = request.POST.get('glucose')
        blood_pressure = request.POST.get('bloodpressure')
        skin_thickness = request.POST.get('skinthickness')
        insulin = request.POST.get('insulin')
        bmi = request.POST.get('bmi')
        diabetes_pedigree_function = request.POST.get('diabetespedigreefunction')
        age = request.POST.get('age')
        
        # load the model
        import pandas as pd

        try:
            model = pd.read_pickle('notebook/diabetes_model.pkl')
            print('Model loaded')
        except Exception as e:
            print('Model not loaded')
            print(e)


        # Make a prediction
        prediction = model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        


        # Return the result
        return render(request, 'predict.html', {'prediction': prediction})
    
    return render(request, 'predict.html')

    