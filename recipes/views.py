from django.http import HttpResponse
from django.template import loader
from .models import Recipe, CATEGORY_CHOICES

def home(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())

def category(request, category_val):
    template = loader.get_template('category.html')
    category_choices = CATEGORY_CHOICES[category_val]
    category_result = Recipe.objects.all().filter(category=category_val)
    context = {
        'category_choices': category_choices,
        'curr_category': category_val,
        'category_result': category_result,
    }
    return HttpResponse(template.render(context, request))

def recipe(request, id):
    template = loader.get_template('recipe.html')
    recipe_choices = Recipe.objects.get(id=id)
    context = {
        'recipe_choices': recipe_choices,
    }
    return HttpResponse(template.render(context, request))
