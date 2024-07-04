from django.http import HttpResponse
from django.template import loader
from .models import Recipe, CATEGORY_CHOICES

def home(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())

def category(request, category_val):
    category_choices = CATEGORY_CHOICES[category_val]
    curr_category = category_val
    category_result = Recipe.objects.filter(category=category_val)
    template = loader.get_template('category.html')
    context = {
        'category_choices': category_choices,
        'curr_category': curr_category,
        'category_result': category_result,
    }
    return HttpResponse(template.render(context, request))