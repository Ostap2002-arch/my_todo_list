import uuid

from django.shortcuts import render
from slugify import slugify

from .forms import FormCreateCategories, FormCreateTask
from .models import Color, Сategories, Works, FilesTask


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
        user = request.user
        category = Сategories.objects.get(owner=user, slug=slug_categories)
        if request.method == "POST":
            form = FormCreateTask(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                data.update([('owner', user), ('slug', slugify(data['title'], separator='_')+str(uuid.uuid1()))])
                work = Works.objects.create(title = data['title'],
                                     description = data['description'],
                                     priority = data['priority'],
                                     date_tasks = data['date_task'],
                                     to_warn = data['to_warn'],
                                     owner = data['owner'],
                                     slug = data['slug'],
                                    categories = category
                                     )
                print(work)
                for file in data['files']:
                    print(file)
                    FilesTask.objects.create(file = file,
                                             task = work)

        # form = CustomForm(initial={'Email': GetEmailString()})
        list_tasks_categories = list(Works.objects.filter(owner=user, categories=category))
        forms = list()
        for task in list_tasks_categories:
            form_new = FormCreateTask(initial={'title' : task.title,
                                               'description': task.description,
                                               'priority': task.priority,
                                               'date_task': task.date_tasks,
                                               'to_warn': task.to_warn,
                                               'files': task.fileds,
                                               })
            forms.append(form_new)
        form = FormCreateTask()
        return render(request, 'todo/show_all_tasks_categories.html', {'works' : list_tasks_categories,
                                                                                            'category' : category,
                                                                                            'form' : form,
                                                                                            'list_forms' : forms
                                                                                                })
    except Exception as s:
        print(s)
        print(slug_categories)


