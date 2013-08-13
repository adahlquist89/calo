from django.db import models

class Group(models.Model):
	STATUS_CHOICES = (
		('OP', 'Opened'),
		('FU', 'Full'),
		('CL', 'Closed')
	)


	name = models.CharField(max_length=255) # arbitrario
	description = models.TextField()
	owner = models.ForeignKey('users.CaloUser')
	limit_size = models.IntegerField() # lo define el usuario
	members = models.ManyToManyField('users.CaloUser')
	creation_date = models.DateTimeField(auto_now_add=True) # al momento de crearse se setea automaticamente el tiempo como 'ahora', usa datetime.datetime
	status = models.CharField(max_length=2,choices=STATUS_CHOICES,default='OP')
