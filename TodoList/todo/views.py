from django.shortcuts import render

from .forms import FormCreateCategories
from .models import Color, Сategories, Works


def new_page(request):
    return render(request, 'todo/index.html')

def create_categories(request):
    if request.method == "POST":
        form = FormCreateCategories(request.POST)
        if form.is_valid():
            result = form.cleaned_data
            result.update([('owner', request.user)])
            try:
                Сategories.objects.create(**result)
            except Exception as ex:
                print(ex)
    form = FormCreateCategories()
    categories = Сategories.objects.filter(owner = request.user).order_by("-date_creat")[:3]
    return render(request, 'todo/create_categoriest_test.html', {'form' : form,
                                                                                      'categories' : categories,
                                                                                        })

def show_all_categories(request):
    categories = Сategories.objects.filter(owner=request.user)
    return render(request, 'todo/show_all_categories.html', {
                                                                 'categories': categories,
                                                                 })
def create_and_show_tasks(request, slug_categories):
    try:
        user = request.user
        category = Сategories.objects.filter(owner=request.user, slug_categories = slug_categories)
        list_tasks_categories = Works.objects.filter(owner = user)
        "Тестовая попытка"
    except Exception as s:
        print(s)

