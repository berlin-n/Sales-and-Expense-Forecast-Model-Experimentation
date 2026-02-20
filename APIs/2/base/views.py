from django.shortcuts import render
from django.http import JsonResponse
from .models import Prediction
from .serializers import PredictionSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
from .forms import PredictionForm

# Create your views here.
scaler = MinMaxScaler()
def df_to_X(df):
    X = []
    X.append(df)
    return np.array(X)

def expense_prediction(unit):
    model = load_model('Expenses Prediction Model/')
    scaled_data = scaler.fit_transform(unit)
    X = df_to_X(scaled_data)
    model_predictions = model.predict(X)
    prediction = scaler.inverse_transform(model_predictions).flatten()
    return prediction

def sales_prediction(unit):
    model = load_model('Sales Prediction Model/')
    sales = np.array(unit).reshape(-1,1)
    scaled_data = scaler.fit_transform(sales)
    model_predictions = model.predict(scaled_data)
    prediction = scaler.inverse_transform(model_predictions).flatten()
    return prediction

@api_view(['GET'])
def data(request):
    if request.method == 'GET':
        predictions = Prediction.objects.all()
        serializer = PredictionSerializer(predictions, many=True)
        return JsonResponse({'predictions': serializer.data})

@api_view(['POST'])
def expns(request):
    if request.method == 'POST':
        months_str = request.data.get('months')
        months = np.array(months_str.split(',')).reshape(-1,1)
        prediction = expense_prediction(months)
        print(prediction)
        return Response(prediction)

@api_view(['POST'])
def sls(request):
    if request.method == 'POST':
        months = float(request.data.get('months', []))
        # month2 = float(request.POST.get('month2', 0))
        # month3 = float(request.POST.get('month3', 0))
        # month4 = float(request.POST.get('month4', 0))
        # data = {'month1':[month1], 'month2':[month2], 'month3':[month3], 'month4':[month4]}
        df = pd.DataFrame(data)
        prediction = sales_prediction(months)
        print(prediction)
    # form = PredictionForm()
    # return render(request, 'base/form.html', {'form': form})