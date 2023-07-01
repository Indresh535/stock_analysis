from django.contrib import admin
from django.urls import path
from AppstockAnalysis import views

urlpatterns = [
    path('', views.index, name='index'),
    path('PlotGraph', views.graphPage, name='graphPage'),
    path('Table_Rows', views.TableRows, name='TableRows'),
    path('Analyze_Data', views.AnalyzeData, name='AnalyzeData'),
    path('UI_Design', views.UiDesign, name='UiDesign'),
]
