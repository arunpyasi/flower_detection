from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.

from .classifier import label
import operator

def index(request):
    return render(request, 'index.html')

    

def detect(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        classfied_dict = classify("media/"+filename)

        detected_flower = max(classfied_dict.items(), key=operator.itemgetter(1))[0]
        print(detected_flower)
        return render(request, 'detect.html', {
            'uploaded_file_url': uploaded_file_url,
            'detected_flower': detected_flower,
        })
    return render(request, 'detect.html')


def classify(file_url):
    classified = label.classify('retrained_graph.pb', file_url, 'retrained_labels.txt', 'final_result', 'Placeholder')
    top_k, labels, results = classified
    classified_dict = {}
    for i in top_k:
        classified_dict[labels[i]]=results[i]

    return classified_dict


def sunflower(request):
    return render(request, 'sunflower.html')

def rose(request):
    return render(request, 'rose.html')

def daisy(request):
    return render(request, 'daisy.html')

def dandelion(request):
    return render(request, 'dandelion.html')

def tulip(request):
    return render(request, 'tulip.html')