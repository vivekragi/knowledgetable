from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import HttpResponse

import openpyxl


def upload1(request):
    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:

        #  Saving POST'ed file to storage
        file = request.FILES['excel_file']
        default_storage.save("staticc/farmer/"+file.name, file)
        # file = request.FILES['excel_file2']
        # default_storage.save("staticc/village/" + file.name, file)
        return HttpResponse("<h1>Uploaded Farmer Successfully</h1>")
        # excel_file = request.FILES["excel_file"]
        #
        # # you may put validations here to check extension or file size
        #
        # wb = openpyxl.load_workbook(excel_file)
        #
        # # getting a particular sheet by name out of many sheets
        # worksheet = wb["Sheet1"]
        # print(worksheet)
        #
        # excel_data = list()
        # # iterating over the rows and
        # # getting value from each cell in row
        # for row in worksheet.iter_rows():
        #     row_data = list()
        #     for cell in row:
        #         row_data.append(str(cell.value))
        #     excel_data.append(row_data)
        #
        # return render(request, 'myapp/template/index.html', {"excel_data": excel_data})
def upload2(request):
    if "GET" == request.method:
        return render(request, 'index1.html', {})
    else:

        #  Saving POST'ed file to storage
        file = request.FILES['excel_file']
        default_storage.save("staticc/village/"+file.name, file)
        # file = request.FILES['excel_file2']
        # default_storage.save("staticc/village/" + file.name, file)
        return HttpResponse("<h1>Uploaded Village Successfully</h1>")
