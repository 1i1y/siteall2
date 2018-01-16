from django.shortcuts import render
from app1.models import table2
from app1 import city
#在views 做資料處理
def prjStateA(request):
    return render(request, "prjStateAll.html")

def prjStateI(request):
    ret1 = table2.objects.all()
    lname = 'kevin1'
    retall = table2.objects.raw('SELECT * FROM app1_table2 WHERE name = %s', [lname])
    ret2 = retall[0]
    State = 'State'
    freq = 'freq'
    產品規劃 = '產品規劃'
    專案管理 = '專案管理'
    產品開發 = '產品開發'
    dict3 = {State: ret2.serializable_value('name'),
             freq: {產品規劃: ret2.serializable_value('prom'),
                    專案管理: ret2.serializable_value('prjm'),
                    產品開發: ret2.serializable_value('prod')}}
    return render(request, "prjStateIndividual.html", {'ret': dict3})

def index(request):
    return render(request, "index.html")
def home(request):
    return render(request, "home.html")
def test(request):

    return render(request, "test2.html")

def index2(request):
    return render(request, "index2.html")


def roc(request):
    return render(request, "roc.html")

def top(request):
    return render(request, "top.html")

def csv(request):
    return render(request, "csv.html")

def maps(request):
    return render(request, "obesityMaps.html")

def blank(request):
    return render(request, "blank.html")

def chart1(request):
    return render(request, "chart1.html")

def chart2(request):
    return render(request, "chart2.html")

def chart3(request):
    return render(request, "chart3.html")

def profile(request):
    return render(request, "profile.html")

def obesityCharts(request):
    return render(request, "obesityCharts.html")
def obesityCharts2(request):
    return render(request, "obesityCharts2.html")
def obesityCharts3(request):
    return render(request, "obesityCharts3.html")

def obesityCharts103(request):
    return render(request, "obesityCharts103.html")

def obesityCharts104(request):
    return render(request, "obesityCharts104.html")

def populationCharts(request):
    return render(request, "populationCharts.html")
def populationCharts2(request):
    return render(request, "populationCharts2.html")

def obesityMaps(request):
	citys=city.get_city()
	areas=city.get_area()
	towns=city.get_town()
	lat=city.get_lat()
	lng=city.get_lng()
	a={'citys':citys,'areas':areas,'towns':towns,'lat':lat,'lng':lng}

	return render(request, "obesityMaps.html",a)

def populationMaps(request):
    return render(request, "populationMaps.html")

