from django.db import models

# Create your models here.

"""docstring for CategoryProd"""
class CategoryProd(models.Model):
	name = models.CharField(max_length=50);
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'categoriaProd'
		verbose_name_plural = 'CategoriasProd'

	def __str__(self):
		return self.name

"""docstring for Products"""
class Products(models.Model):
	name = models.CharField(max_length=255)
	category = models.ForeignKey(CategoryProd, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="shop", null=True, blank=True)
	price = models.FloatField()
	availability = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Products'
	
	def __str__(self):
		return self.name