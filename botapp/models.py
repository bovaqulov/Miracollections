from django.db import models

class TgUser(models.Model):
	tg_id = models.BigIntegerField()
	is_admin = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.tg_id}"


class Button(models.Model):
	title = models.CharField(max_length=255)
	img = models.ImageField(upload_to="button_img/", null=True, blank=True)
	text = models.TextField(default="notext", null=True, blank=True)

	def __str__(self):
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.title


class Blinds(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title  = models.CharField(max_length=200)
	text = models.TextField(default="Text")
	img = models.ImageField(upload_to="blinds_img/")

	def __str__(self):
		return self.title







