# Generated by Django 5.1.1 on 2024-09-06 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=300)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('blood_type', models.CharField(choices=[('A+', 'A+Ve'), ('A-', 'A-Ve'), ('B+', 'B+Ve'), ('B-', 'B-Ve'), ('AB+', 'AB+Ve'), ('AB-', 'AB-Ve'), ('O+', 'O+Ve'), ('O-', 'O-Ve'), ('Oh+', 'Oh+Ve'), ('Oh-', 'Oh-Ve')], max_length=3)),
                ('blood_component', models.CharField(choices=[('whole Blood', 'whole Blood'), ('single Donor platelet', 'single Donor platelet'), ('single Donor plasma', 'single Donor plasma'), ('sagm packed Red Blood cells', 'sagm packed Red Blood cells'), ('Random Donor platelets', 'Random Donor platelets'), ('plasma', 'plasma'), ('platelets Rich Plasma', 'platelets Rich Plasma'), ('Leukoreduced Rbc', 'Leukoreduced Rbc'), ('cryoprecipitate', 'cryoprecipitate'), ('Fresh Frozen Plasma', 'Fresh Frozen Plasma')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('Oh+', 'Oh+'), ('Oh-', 'Oh-'), ('O+', 'O+'), ('O-', 'O-')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=10)),
                ('donation_date', models.DateField()),
            ],
        ),
    ]