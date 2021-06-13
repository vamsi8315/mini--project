from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import date

# Create your models here.

class ImPfle(models.Model):
	g=[('Male','Male'),('Female','Female')]
	add = [('Amaravathi','Amaravathi'),('Bantumilli','Bantumilli'),('Bhimavaram','Bhimavaram'),('Eluru','Eluru'),('Gudivada','Gudivada'),('Gudlavalleru','Gudlavalleru'),('Machilipatnam','Machilipatnam'),('Kakinada','Kakinada'),('Kurnool','Kurnool'),('Kadapa','Kadapa'),('Rajahumandry','Rajahumandry'),('Sriharikota','Sriharikota'),('Vijayawada','Vijayawada'),('Vizag','Vizag')]
	u = models.OneToOneField(User,on_delete=models.CASCADE)
	im = models.ImageField(upload_to="Profile/",null=True,default="blank-profile-picture.png")
	Address = models.CharField(choices=add,max_length=15,null=True)
	date_of_birth = models.DateField(null=True)
	mb = models.CharField(max_length=10)
	gender=models.CharField(max_length=10,choices=g)

@receiver(post_save,sender=User)
def Crtpfle(sender,instance,created,**kwrgs):
	if created:
		ImPfle.objects.create(u=instance)


class Data(models.Model):
	busclas = [('Pallevellugu','Pallevellugu'),('Express','Express'),('Ultra Deluxe','Ultra Deluxe')]
	source = models.CharField(max_length=30)
	destination = models.CharField(max_length=30)
	busid = models.CharField(max_length=10)
	busim = models.ImageField(upload_to="Bus_Image/",null=True,default="bus.jpg")
	distance = models.CharField(max_length=10,null=True)
	cost = models.CharField(max_length=15,null=True)
	timmings = models.CharField(max_length=30)
	d = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	busclass = models.CharField(max_length=15,choices=busclas)
	da =   models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.source + self.destination
	class Meta:
		db_table = 'data'

class PassengerData(models.Model):
	bty = [('Pallevellugu','Pallevellugu'),('Express','Express'),('Ultra Deluxe','Ultra Deluxe')]
	pname = models.CharField(max_length=30,null=True)
	m = models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(("Date"), default=date.today)
	bustype = models.CharField(max_length=30,null=True,choices=bty)
	sorce = models.CharField(max_length=30,null=True)
	destnation = models.CharField(max_length=30,null=True)
	busid = models.IntegerField(null=True)