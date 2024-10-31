from django.db import models

class BloodBank(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(max_length=300)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+Ve'),
        ('A-', 'A-Ve'),
        ('B+', 'B+Ve'),
        ('B-', 'B-Ve'),
        ('AB+', 'AB+Ve'),
        ('AB-', 'AB-Ve'),
        ('O+', 'O+Ve'),
        ('O-', 'O-Ve'),
        ('Oh+', 'Oh+Ve'),
        ('Oh-', 'Oh-Ve'),
    ]
    
    BLOOD_COMPONENT_CHOICES = [
        ('whole Blood', 'whole Blood'),
        ('single Donor platelet', 'single Donor platelet'),
        ('single Donor plasma', 'single Donor plasma'), 
        ('sagm packed Red Blood cells', 'sagm packed Red Blood cells'),
        ('Random Donor platelets', 'Random Donor platelets'), 
        ('plasma', 'plasma'),
        ('platelets Rich Plasma', 'platelets Rich Plasma'), 
        ('Leukoreduced Rbc', 'Leukoreduced Rbc'),
        ('cryoprecipitate', 'cryoprecipitate'), 
        ('Fresh Frozen Plasma', 'Fresh Frozen Plasma')
    ]
    
    blood_type = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    blood_component = models.CharField(max_length=50, choices=BLOOD_COMPONENT_CHOICES)

    def __str__(self):
        return self.name



class Donor(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('Oh+', 'Oh+'),
        ('Oh-', 'Oh-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    donation_date=models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



