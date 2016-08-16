from django.db import models

class Afectado(models.Model):
	id_afectado = models.AutoField(primary_key=True)
	cedula_afectado = models.CharField(max_length = 10)
	telf_afectado = models.CharField(max_length = 16)
	nombre_afectado = models.CharField(max_length = 32)
	apellido_afectado = models.CharField(max_length = 32)
	direccion_afectado = models.TextField()
	"""docstring for Afectado"""
	def envio(self):
		self.save()
	def __str__(self):
		return '%s %s' % (self.nombre_afectado, self.apellido_afectado)

class Denuncia(models.Model):
	id_denuncia = models.AutoField(primary_key=True)
	id_afectado = models.ForeignKey(Afectado)
	movil_denuncia = models.CharField(max_length = 16)
	lugar_denuncia = models.CharField(max_length = 32)
	fecha_denuncia = models.DateField()
	hora_denuncia = models.TimeField()
	direccion_denuncia = models.TextField()
	"""docstring for Denuncia"""
	def guardado(self):
		self.save()
	def __str__(self):
		return self.lugar_denuncia

class Sospechoso(models.Model):
	id_sospechoso = models.AutoField(primary_key=True)
	id_denuncia = models.ForeignKey(Denuncia)
	nombre_sospechoso = models.CharField(max_length = 32)
	apellido_sospechoso = models.CharField(max_length = 32)
	sexo_sospechoso = models.CharField(max_length = 10)
	edad_sospechoso = models.IntegerField()
	piel_sospechoso = models.CharField(max_length = 16) 
	estatura_sospechoso = models.FloatField()
	contextura_sospechoso = models.CharField(max_length = 32)
	cabello_sospechoso = models.CharField(max_length = 32)
	color_cabello_sospechoso = models.CharField(max_length = 32)
	color_ojos_sospechoso = models.CharField(max_length = 32)
	nariz_sospechoso = models.CharField(max_length = 32)
	forma_rostro_sospechoso = models.CharField(max_length = 32)
	senial_sospechoso = models.CharField(max_length = 32)
	bello_facial_sospechoso = models.CharField(max_length = 32)
	bosquejo_sospechoso = models.ImageField(upload_to='img_sospechoso/')
	"""docstring for Sospechoso"""
	def guardado(self):
		self.save()
	def __str__(self):
		return '%s %s' % (self.nombre_sospechoso, self.apellido_sospechoso)

class Delincuente(models.Model):
	id_delincuente = models.AutoField(primary_key=True)
	nombre_delincuente = models.CharField(max_length = 32)
	apellido_delincuente = models.CharField(max_length = 32)
	sexo_delincuente = models.CharField(max_length = 10)
	edad_delincuente = models.IntegerField()
	piel_delincuente = models.CharField(max_length = 16) 
	estatura_delincuente = models.FloatField()
	contextura_delincuente = models.CharField(max_length = 32)
	cabello_delincuente = models.CharField(max_length = 32)
	color_cabello_delincuente = models.CharField(max_length = 32)
	color_ojos_delincuente = models.CharField(max_length = 32)
	nariz_delincuente = models.CharField(max_length = 32)
	forma_rostro_delincuente = models.CharField(max_length = 32)
	senial_delincuente = models.CharField(max_length = 32)
	bello_facial_delincuente = models.CharField(max_length = 32)
	foto_delincuente = models.ImageField(upload_to='img_delincuente/')
	"""docstring for Delincuente"""
	def guardado(self):
		self.save()
	def __str__(self):
		return '%s %s' % (self.nombre_delincuente, self.apellido_delincuente)

class Sospecha(models.Model):
	id_sospechoso = models.ForeignKey(Sospechoso)
	id_delincuente = models.ForeignKey(Delincuente)	
	"""docstring for Sospecha"""
	class Meta:
		unique_together = (('id_sospechoso','id_delincuente'),)