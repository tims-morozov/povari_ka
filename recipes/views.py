from django.http import HttpResponse
from django.template import loader
from .models import Recipe, CATEGORY_CHOICES, Ingredient, Step, Serving

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
    ingredients = Ingredient.objects.all().filter(recipe = id)
    steps = Step.objects.all().filter(recipe = id)
    serving = Serving.objects.get(recipe = id)

    context = {
        'recipe_choices': recipe_choices,
        'ingredients': ingredients,
        'steps': steps,
        'serving': serving,
    }

    return HttpResponse(template.render(context, request))

def contacts(request):
    template = loader.get_template('contacts.html')

    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')

    return HttpResponse(template.render())