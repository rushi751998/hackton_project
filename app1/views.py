from django.shortcuts import render, HttpResponse, redirect
from .forms import Video_form
from .models import Video
import datetime
import pandas as pd
import json

# def index(request):
#     all_video=Video.objects.all()
#     if request.method == "POST":
#         form=Video_form(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request,'index.html')
#     else:
#         form=Video_form()
#         return render(request,'index.html',{"form":form})


def index(request):
    return render(request, 'index.html')


def videos(request):
    all_video = Video.objects.all()
    date = datetime.datetime.today().date()
    return render(request, 'videos1.html', {"all": all_video, "date": date})


def videos2(request):
    all_video = Video.objects.all()
    date = datetime.datetime.today().date()
    return render(request, 'videos2.html', {"all": all_video, "date": date})


def dashboard(request):

    data = pd.read_csv('processed.csv')
    data.columns = data.columns.str.replace(" ","_")
    col_name = data.columns

    json_records = data.reset_index().to_json(orient='records')
    data_html = json.loads(json_records)

    emotions_lables = data['Emotion'].unique()
    emotions_values = data.groupby('Emotion').count()['Age'].values

    gender = data['Gender'].unique()
    gender_values = data.groupby('Gender').count()['Age'].values

    activity = data['Suspecious'].unique()
    activity_values = data.groupby('Suspecious').count()['Emotion'].values

    # param = {'all':range(4),"chart_fields":df}
    param = {'col_name': col_name,
             "data_html": data_html,
             'all': range(4),
             "emotions_lables": emotions_lables, 'emotions_values': emotions_values,
             'gender': gender, 'gender_values': gender_values,
             'activity': activity, 'activity_values': activity_values,

             }
    return render(request, 'dashboard.html', param)
