from django.urls import reverse_lazy
from django.shortcuts import redirect


def add_one(pk, Model):
    comment_total = Model.objects.get(pk=pk)
    comment_total.likes += 1
    comment_total.save()
    return comment_total
