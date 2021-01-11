from django.urls import reverse_lazy
from django.shortcuts import redirect


def add_one(pk, Model):
    like_total = Model.objects.get(pk=pk)
    like_total.likes += 1
    like_total.save()
    return like_total