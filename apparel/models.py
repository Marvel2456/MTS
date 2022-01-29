from tkinter import CASCADE
from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=250, unique=True, db_index=True)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return self.customer_name

class Male(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    shirt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    burst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sleeve = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    round_sleeve = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shoulder = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    waist = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    flap = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    trouser_length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    thigh = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    calf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    instep = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    choices = (
        ('Inches', 'inches'),
        ('Centimeter', 'cm'),
    )
    unit = models.CharField(max_length=50, choices=choices, default="inches")
    
    
    def __str__(self):
        return self.customer.customer_name  

class Female(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    burst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    under_burst = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    waist = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    half_length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sleeve = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    round_sleeve = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    breast_point = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nipple_to_nipple = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    skirt_length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    waist_hip = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    flap = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    thigh = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    calf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    instep = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    blouse = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shoulder = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    choices = (
        ('Inches', 'inches'),
        ('Centimeter', 'cm'),
    )
    unit = models.CharField(max_length=50, choices=choices, default="inches")
      
    def __str__(self):
        return self.customer.customer_name
    
class Staff(models.Model):
    staff_name = models.CharField(max_length=250, unique=True, db_index=True)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    FRONT_DESK = 'FRD'
    SECRETARY = 'SEC'
    TAILOR = 'TLR'
    OTHERS = 'OTH'
    STAFF_CATEGORY_CHOICE = [
        (FRONT_DESK, 'FRD'),
        (TAILOR, 'TLR'),
        (SECRETARY, 'SEC'),
        (OTHERS, 'OTH')
    ]
    staff_category = models.CharField(max_length=3, choices=STAFF_CATEGORY_CHOICE, default="TLR")
    
    def __str__(self):
        return self.staff_name
    
class Tailor(models.Model):
    tailor_name = models.ForeignKey(Staff, on_delete=models.CASCADE,  blank=False)
    MALE = 'M'
    FEMALE = 'F'
    CLOTHES_STYLE_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE')
    ]
    clothe_style = models.CharField(max_length=1, choices=CLOTHES_STYLE_CHOICES, default="MALE")
    def __str__(self):
        return self.tailor_name.staff_name
    
class Appointments(models.Model):
    customer = models.CharField(max_length=250)
    date = models.DateTimeField()
    tailor = models.ForeignKey(Tailor, on_delete=models.CASCADE, blank=False)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.tailor.tailor_name
    
class Clothes(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    is_complete = models.BooleanField(default=False)
    in_progress = models.BooleanField(default=True)
    date_completed = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.customer.customer_name
    
class RegisterIn(models.Model):
    staff_name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    clock_in_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.clock_in_time)
    
    
class RegisterOut(models.Model):
    staff_name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    clock_out_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.clock_out_time)
    
        
class Entry(models.Model):
    date = models.DateField(auto_now_add=True)
    clock_in = models.ManyToManyField(RegisterIn)
    clock_out = models.ManyToManyField(RegisterOut)
    def __str__(self):
        return str(self.date)
    
class Style(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/pics')
    desc = models.CharField(max_length=250)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
