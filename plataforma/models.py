from django.db import models

class Livros(models.Model):
  nome = models.CharField(max_length=100)
  descricao = models.TextField()
  n_paginas = models.IntegerField()

  def __str__(self):
    return self.nome

  class Meta:
    verbose_name = 'Livros'
    verbose_name_plural = 'Livros'