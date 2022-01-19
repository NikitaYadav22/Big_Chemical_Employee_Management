# Generated by Django 3.1.6 on 2021-12-06 04:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('cName', models.CharField(max_length=50, primary_key='true', serialize=False, unique='true')),
                ('cEmail', models.EmailField(max_length=254)),
                ('cLogo', models.ImageField(blank=True, upload_to='images')),
                ('cUrl', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('eFname', models.CharField(max_length=50)),
                ('eLname', models.CharField(max_length=50)),
                ('eDepartment', models.CharField(max_length=10)),
                ('eEmail', models.CharField(max_length=40)),
                ('ePhone', models.IntegerField(blank=True, null=True)),
                ('eState', models.CharField(max_length=25)),
                ('eCity', models.CharField(max_length=25)),
                ('eZip', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='SensorDetails',
            fields=[
                ('sID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('sInstallationDate', models.CharField(max_length=10)),
                ('sDepartment', models.CharField(max_length=10)),
                ('sName', models.CharField(max_length=25)),
                ('sLocation', models.CharField(default='', max_length=5)),
                ('sFloor', models.IntegerField(blank=True, null=True)),
                ('sRoom', models.IntegerField(blank=True, null=True)),
                ('sDirection', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'sensor_details',
            },
        ),
        migrations.CreateModel(
            name='TrackingLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eAction', models.CharField(default='', max_length=5)),
                ('sTime', models.DateField(auto_now_add=True)),
                ('eID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mirai.employee')),
                ('sID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mirai.sensordetails')),
            ],
            options={
                'db_table': 'tracking_log',
            },
        ),
        migrations.CreateModel(
            name='SensorRepairLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sDateDown', models.CharField(max_length=10)),
                ('sDateRestored', models.CharField(default='Not Yet', max_length=10)),
                ('sTechnician', models.CharField(max_length=25)),
                ('sCause', models.CharField(max_length=100)),
                ('sRepaired', models.CharField(max_length=10)),
                ('sID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mirai.sensordetails')),
            ],
            options={
                'db_table': 'sensor_repair_log',
            },
        ),
        migrations.CreateModel(
            name='DrugTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labID', models.CharField(default='', max_length=20)),
                ('result', models.CharField(max_length=20)),
                ('labTest', models.CharField(max_length=25)),
                ('tDate', models.DateField()),
                ('eID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mirai.employee')),
            ],
            options={
                'db_table': 'drug_test',
            },
        ),
    ]
