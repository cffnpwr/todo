from django.db import models


class ToDoListManager(models.Manager):
    def create_todo(self, request_data):
        todo = self.model(
            title=request_data['title'], detail=request_data['detail'], checked=request_data['checked'])
        todo.save()
        return todo


class ToDoList(models.Model):
    title = models.CharField(max_length=256)
    detail = models.TextField()
    checked = models.BooleanField(default=False)
    objects = ToDoListManager()
