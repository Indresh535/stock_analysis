import contextlib
from django.shortcuts import render, HttpResponse, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from collections import Counter
import os
import pandas as pd
import numpy as np
from pandas._libs import missing
from pandas.core.indexing import check_bool_indexer

# Create your views here.
def index(request):
    global column_id,clean_data,file_directory
    # return HttpResponse('This is index Page')
    if request.method == 'POST':
        uploaded_files=request.FILES['choose_csv']
        clean_data = request.POST.get('clean_data')
        print(clean_data)
        print(uploaded_files)
        
        if uploaded_files.name.endswith('csv'):
            save_file=FileSystemStorage()
            name_file=save_file.save(uploaded_files.name, uploaded_files) #this is name of the file            
            current_directory=os.getcwd()    #To get the current directory of the folder
            file_directory=current_directory+'\media\\'+name_file
            readFile(file_directory)
            return cleanData(request)
         
    return render(request,'index.html')



def readFile(filename):
    global rows,columns,my_file,data,missing_values,data_html
    my_file = pd.read_csv(filename, sep=',',engine='python')       #using to read the csv file with columns seperators of delimitor(,)
    data=pd.DataFrame(data=my_file,index=None)
    data_html = data.to_html()
    context = {'loaded_data': data_html,}
    print(data)
    
    
    #rows and columns
    rows=len(data.axes[0])              # to count number of rows
    columns=len(data.axes[1])            # to count number of columns
    
    # finding missing values
    missing_signs = ['?','0','--']
    null_data = data[data.isnull().any(axis=1)]             # To finding the null values
    missing_values=len(null_data) 
    
    
    
# ****************************** Function for cleaning the Data  **************************************
def cleanData(request):     
    null_message = "found " + str(rows) + " rows " + str(columns) + " and columns.\nMissing data are: " + str(missing_values)
    context = {
        'loaded_data': data_html,
        'cleanMessage':null_message,
    }
    messages.warning(request, null_message) 
                
    return render(request,'index.html')
    
    
# ************************************  Function for Graph Plotting  in graph_page.html *********************************
    
def graphPage(request):
    global column_id,clean_data,file_directory
    if request.method == 'POST':
        uploaded_files=request.FILES['choose_csv']
        column_id = request.POST.get('column_id')
        print(uploaded_files)
        print(column_id)
        
        if uploaded_files.name.endswith('csv'):
            save_file=FileSystemStorage()
            name_file=save_file.save(uploaded_files.name, uploaded_files) #this is name of the file            
            current_directory=os.getcwd()    #To get the current directory of the folder
            file_directory=current_directory+'\media\\'+name_file
            readFile(file_directory)
            return graphPlotPage(request)
        
    return render(request,'graph_page.html')




def readFile(filename):
    global rows,columns,my_file,data,missing_values,data_html
    my_file = pd.read_csv(filename, sep=',',engine='python')       #using to read the csv file with columns seperators of delimitor(,)
    data=pd.DataFrame(data=my_file,index=None)
    data_html = data.to_html()
    context = {'loaded_data': data_html,}
    print(data)
    
    
    #rows and columns
    rows=len(data.axes[0])              # to count number of rows
    columns=len(data.axes[1])            # to count number of columns
    
    # finding missing values
    missing_signs = ['?','0','--']
    null_data = data[data.isnull().any(axis=1)]             # To finding the null values
    missing_values=len(null_data) 
    
    
    
            
def graphPlotPage(request):
    dashboard = []
    
    for x in data[column_id]:           # Go to the specified input column_id row by row and saved this in the dashboard array[]
        dashboard.append(x)
        
    my_dashboard = dict(Counter(dashboard))
    print('my dashboard',my_dashboard)
    
    keys = my_dashboard.keys()
    values = my_dashboard.values()
    
    listkeys = []
    listvalues = []
    
    for x in keys:
        listkeys.append(x)
     
    for y in values:
        listvalues.append(y)
        
    context = {
        'listkeys':listkeys,
        'listvalues':listvalues,        
    }            
    return render(request,'graph_page.html',context)

# ****************************** Function for Displaying the CSV Table Rows  ***********************************

def TableRows(request):
    global column_id,clean_data,file_directory
    if request.method == 'POST':
        uploaded_files=request.FILES['choose_csv']
        numrows = request.POST.get('numrows')
        numrows=int(numrows)
        print(numrows)
        
        if uploaded_files.name.endswith('csv'):
            save_file=FileSystemStorage()
            name_file=save_file.save(uploaded_files.name, uploaded_files) #this is name of the file            
            current_directory=os.getcwd()    #To get the current directory of the folder
            file_directory=current_directory+'\media\\'+name_file
            my_file = pd.read_csv(file_directory, sep=',',engine='python')       #using to read the csv file with columns seperators of delimitor(,)
            data=pd.DataFrame(data=my_file,index=None)
            # data_html = data.to_html()
            firstRows=data.head(numrows).to_html()
            lastRows=data.tail(5).to_html()
            context={
                'firstRow':firstRows,
                'lastRow':lastRows,
            }
            return HttpResponse(firstRows)
    return render(request,'table.html')





def AnalyzeData(request):
    return render(request,'analyseData.html')
    
def UiDesign(request):
    return HttpResponse(request,'uiDesign.html') 




# ****************************** Function for Displaying the Graph  ***********************************

    
# def graphPage(request):
#     # null_message = 'Found ' + str(rows) + ' rows and ' + str(columns) + ' columns. Missing data are: ' + str(missing_values)
#     # messages.warning(request, null_message) 
#     # split  into keys and values based on the attribute input
#     dashboard = []
    
#     for x in data[column_id]:           # Go to the specified input column_id row by row and saved this in the dashboard array[]
#         dashboard.append(x)
        
#     my_dashboard = dict(Counter(dashboard))
#     print('my dashboard',my_dashboard)
    
#     keys = my_dashboard.keys()
#     values = my_dashboard.values()
    
#     listkeys = []
#     listvalues = []
    
#     for x in keys:
#         listkeys.append(x)
     
#     for y in values:
#         listvalues.append(y)
        
#     context = {
#         'listkeys':listkeys,
#         'listvalues':listvalues,        
#     }
            
#     return render(request,'graph_page.html',context)


























# ***********************************************************************************

# Create your views here.
# def index(request):
#     global column_id,clean_data,file_directory
#     # return HttpResponse('This is index Page')
#     if request.method == 'POST':
#         uploaded_files=request.FILES['choose_csv']
#         column_id = request.POST.get('column_id')
#         clean_data = request.POST.get('clean_data')
#         print(clean_data)
#         print(uploaded_files)
#         print(column_id)
        
#         if uploaded_files.name.endswith('csv'):
#             save_file=FileSystemStorage()
#             name_file=save_file.save(uploaded_files.name, uploaded_files) #this is name of the file            
#             current_directory=os.getcwd()    #To get the current directory of the folder
#             file_directory=current_directory+'\media\\'+name_file
#             readFile(file_directory)
#             return cleanData(request)
         
#     return render(request,'index.html')




# def readFile(filename):
#     global rows,columns,my_file,data,missing_values,data_html
#     my_file = pd.read_csv(filename, sep=',',engine='python')       #using to read the csv file with columns seperators of delimitor(,)
#     data=pd.DataFrame(data=my_file,index=None)
#     data_html = data.to_html()
#     context = {'loaded_data': data_html,}
#     print(data)
    
    
#     #rows and columns
#     rows=len(data.axes[0])              # to count number of rows
#     columns=len(data.axes[1])            # to count number of columns
    
#     # finding missing values
#     missing_signs = ['?','0','--']
#     null_data = data[data.isnull().any(axis=1)]             # To finding the null values
#     missing_values=len(null_data) 
    
    
    
# # ****************************** Function for cleaning the Data  **************************************
# def cleanData(request):     
#     null_message = 'found ' + str(rows) + 'rows ' + str(columns) + 'and columns. Missing data are: ' + str(missing_values)
#     context = {
#         'loaded_data': data_html,
#         'cleanMessage':null_message,
#     }
#     messages.warning(request, null_message) 
                
#     return render(request,'index.html')
    
    
# # ****************************** Function for Displaying the Graph  ***********************************

    
# def graphPage(request):
#     null_message = 'Found ' + str(rows) + ' rows and ' + str(columns) + ' columns. Missing data are: ' + str(missing_values)
#     messages.warning(request, null_message) 
#     # split  into keys and values based on the attribute input
#     dashboard = []
    
#     for x in data[column_id]:           # Go to the specified input column_id row by row and saved this in the dashboard array[]
#         dashboard.append(x)
        
#     my_dashboard = dict(Counter(dashboard))
#     print('my dashboard',my_dashboard)
    
#     keys = my_dashboard.keys()
#     values = my_dashboard.values()
    
#     listkeys = []
#     listvalues = []
    
#     for x in keys:
#         listkeys.append(x)
     
#     for y in values:
#         listvalues.append(y)
        
#     context = {
#         'listkeys':listkeys,
#         'listvalues':listvalues,        
#     }
            
#     return render(request,'graph_page.html',context)
