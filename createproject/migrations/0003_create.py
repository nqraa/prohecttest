# Generated by Django 3.0.7 on 2020-06-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createproject', '0002_createproject_contr_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('contract_number', models.DecimalField(decimal_places=0, max_digits=14)),
                ('contract_date', models.DateField()),
                ('contr_name', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=50)),
            ],
        ),
    ]
