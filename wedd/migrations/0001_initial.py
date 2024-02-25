# Generated by Django 3.2.22 on 2024-02-05 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MatrimonialProfile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(upload_to='profile_pics/')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('height', models.FloatField()),
                ('date_of_birth', models.DateField()),
                ('birth_time', models.TimeField()),
                ('birth_place', models.CharField(max_length=100)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=20)),
                ('caste', models.CharField(default='Wandekar Kunbi', max_length=50)),
                ('country_living', models.CharField(max_length=50)),
                ('state_living', models.CharField(max_length=50)),
                ('city_living', models.CharField(max_length=50)),
                ('permanent_address', models.TextField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_created_by', models.CharField(max_length=50)),
                ('languages_spoken', models.CharField(max_length=100)),
                ('disability', models.BooleanField(default=False)),
                ('about_education', models.TextField(blank=True, null=True)),
                ('highest_education', models.CharField(blank=True, max_length=100, null=True)),
                ('pg_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('pg_college', models.CharField(blank=True, max_length=100, null=True)),
                ('ug_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('ug_college', models.CharField(blank=True, max_length=100, null=True)),
                ('school_name', models.CharField(blank=True, max_length=100, null=True)),
                ('about_career', models.TextField(blank=True, null=True)),
                ('employed_in', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=100, null=True)),
                ('about_family', models.TextField(blank=True, null=True)),
                ('father_occupation', models.CharField(max_length=100)),
                ('mother_occupation', models.CharField(max_length=100)),
                ('brothers', models.PositiveIntegerField()),
                ('sisters', models.PositiveIntegerField()),
                ('married_sisters', models.PositiveIntegerField()),
                ('living_with_parents', models.BooleanField(default=False)),
                ('family_based_city', models.CharField(max_length=50)),
                ('maternal_uncles_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_no', models.CharField(max_length=15)),
                ('lifestyle', models.TextField(blank=True, null=True)),
                ('drinking_habits', models.BooleanField(default=False)),
                ('smoking_habits', models.BooleanField(default=False)),
                ('biodata', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('is_phone_visible', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_interactions', to='wedd.matrimonialprofile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_interactions', to='wedd.matrimonialprofile')),
            ],
        ),
    ]