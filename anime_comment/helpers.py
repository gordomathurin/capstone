from django.urls import reverse_lazy
from django.shortcuts import redirect

def add_one(pk, Model):
    vote = Model.objects.get(pk=pk)
    vote.likes += 1
    vote.save()
    return vote
