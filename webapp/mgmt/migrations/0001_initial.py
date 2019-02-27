# Generated by Django 2.1.7 on 2019-02-22 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('hire_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mgmt.Departments')),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(default='Lancaster', max_length=50)),
                ('state', models.CharField(default='PA', max_length=2)),
                ('zip', models.IntegerField(default=17603)),
            ],
        ),
    ]