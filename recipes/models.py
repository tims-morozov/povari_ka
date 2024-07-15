from django.db import models

CATEGORY_CHOICES = {
    "soup": "Первые блюда",
    "second_course": "Вторые блюда",
    "salad": "Салаты",
    "grill": "Мангал",
    "dessert": "Десерты",
    "drink": "Напитки",
}

class Recipe(models.Model):
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='')
    name = models.CharField(max_length=250, default='')
    description = models.CharField(max_length=150, default='')
    image = models.ImageField(upload_to='images', blank=True, null=True, default='Recipe Image')

    def __str__(self):
        self.name = self.name.capitalize()
        return f"{self.name} (id: {self.id})" 
 

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    ingredient = models.CharField(max_length=500)
    
    def __str__(self):
        return f"ingredients for {self.recipe}"
    

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    step_number = models.IntegerField() 
    description = models.CharField(max_length=1200)
    image = models.ImageField(upload_to='images', default='')
    
    def __str__(self):
        return f"steps for {self.recipe}"
    

class Serving(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE, default='')
    description = models.CharField(max_length=800)
    image = models.ImageField(upload_to='images', default='')

    def __str__(self):
        return f"serving for {self.recipe}"