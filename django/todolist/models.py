from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

from user.models import Account


# class ToDoListManager(models.Manager):
    # def create_todo(self, request_data):
    #     todo = self.model(
    #         user=request_data['user'], title=request_data['title'], detail=request_data['detail'], checked=request_data['checked'])
    #     todo.save()
    #     return todo


class ToDoList(models.Model):
    user = models.CharField(max_length=256)
    # user = models.ForeignKey(Account, on_delete=CASCADE)
    title = models.CharField(max_length=256)
    detail = models.TextField()
    checked = models.BooleanField(default=False)
    # objects = ToDoListManager()
