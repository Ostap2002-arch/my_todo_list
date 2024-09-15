
from django.shortcuts import render
from slugify import slugify

from .forms import FormCreateCategories, FormCreateTask
from .models import Color, Сategories, Works


def new_page(request):
    return render(request, 'todo/index.html')

def create_categories(request):
    if request.method == "POST":
        form = FormCreateCategories(request.POST)
        if form.is_valid():
            result = form.cleaned_data
            result.update([('owner', request.user), ('slug', slugify(result['title'], separator='_').capitalize())])
            try:
                Сategories.objects.create(**result)
            except Exception as ex:
                print(ex)
    form = FormCreateCategories()
    categories = Сategories.objects.filter(owner = request.user).order_by("-date_creat")[:3]
    first_category = Сategories.objects.filter(owner=request.user).order_by("pk")[0]
    return render(request, 'todo/create_categoriest_test.html', {'form' : form,
                                                                                      'categories' : categories,
                                                                                        'first_category' : first_category,
                                                                                        })

def show_all_categories(request, slug_categories):
    categories = Сategories.objects.filter(owner=request.user)
    return render(request, 'todo/show_all_categories.html', {
                                                                'categories': categories,
                                                                'slug_categories':slug_categories,
                                                                 })
def create_and_show_tasks(request, slug_categories):
    try:
        print(request.POST)
        user = request.user
        category = Сategories.objects.get(owner=user, slug = slug_categories)
        list_tasks_categories = Works.objects.filter(owner = user, categories = category)
        form = FormCreateTask()
        return render(request, 'todo/show_all_tasks_categories.html', {'works' : list_tasks_categories,
                                                                                            'category' : category,
                                                                                            'form' : form,
                                                                                                })
    except Exception as s:
        print(s)
        print(slug_categories)


