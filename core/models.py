from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Element(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  element_name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='element_images')
  description = models.TextField(blank=True)
  creator = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.element_name

STATUS = (
  ('Not started', 'Not started'),
  ('Promotion', 'Promotion'),
  ('Ended', 'Ended')
)

class Promotion(models.Model):
  promotion = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  status = models.CharField(max_length=20, null=True, choices=STATUS)
  date_start = models.DateTimeField(default=datetime.now)
  date_promotion = models.DateTimeField(default=datetime.now)
  date_done = models.DateTimeField(default=datetime.now)
  left_elem = models.ForeignKey(Element, on_delete=models.CASCADE, related_name='elem_1', null=True, default=None)
  right_elem = models.ForeignKey(Element, on_delete=models.CASCADE, related_name='elem_2', null=True, default=None)
  promoted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='promoted', null=True, default=None)
  ended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ended', null=True, default=None)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.promotion

class Vote(models.Model):
  element_id = models.CharField(max_length=100)
  votes_count = models.IntegerField(null=True, default=0)

class Voter(models.Model):
  ip = models.CharField(max_length=100)
  voter_country = models.CharField(max_length=100)
  voter_useragent = models.CharField(max_length=255)
  element_id = models.CharField(max_length=12)
  promotion_id = models.CharField(max_length=10, null=True)
  counrty_code = models.CharField(max_length=2, null=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)