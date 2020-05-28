from django.db import models

# Create your models here.
class Theater(models.Model):
    id_theater = models.AutoField(primary_key=True)
    theater_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'theater'

    def __str__(self):
        return self.theater_name

class Hall(models.Model):
    id_hall = models.AutoField(primary_key=True)
    theaterid = models.ForeignKey('Theater', models.DO_NOTHING, db_column='theaterID')  # Field name made lowercase.
    hall_name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hall'

class Repertoire(models.Model):
    id_repertoire = models.AutoField(primary_key=True)
    performance_name = models.CharField(max_length=100)
    length = models.TimeField()
    description = models.TextField()
    director = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repertoire'

class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    role_description = models.TextField()
    repertoireid = models.ForeignKey(Repertoire, models.DO_NOTHING, db_column='repertoireID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'

class Seance(models.Model):
    id_seance = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    hallid = models.ForeignKey(Hall, models.DO_NOTHING, db_column='hallID')  # Field name made lowercase.
    repertoireid = models.ForeignKey(Repertoire, models.DO_NOTHING, db_column='repertoireID')  # Field name made lowercase.
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'seance'

class Staff(models.Model):
    id_staff = models.AutoField(primary_key=True)
    position = models.CharField(max_length=50)
    staff_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    birthday = models.DateField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    theaterid = models.ForeignKey('Theater', models.DO_NOTHING, db_column='theaterID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staff'

class Actorrole(models.Model):
    id_act_role = models.AutoField(primary_key=True)
    seanceid = models.ForeignKey('Seance', models.DO_NOTHING, db_column='seanceID')  # Field name made lowercase.
    roleid = models.ForeignKey('Role', models.DO_NOTHING, db_column='roleiD')  # Field name made lowercase.
    staffid = models.ForeignKey('Staff', models.DO_NOTHING, db_column='staffID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actorrole'
        
class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_mobile = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'customer'

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    seanceid = models.ForeignKey(Seance, models.DO_NOTHING, db_column='seanceID')  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='customeriD', blank=True, null=True)  # Field name made lowercase.
    place = models.IntegerField(unique=True)
    isreserved = models.CharField(db_column='isReserved', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ticket'

