# Generated by Django 4.1.3 on 2023-01-11 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.class')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('students', models.ManyToManyField(through='class.Enrollment', to='class.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(through='class.Enrollment', to='class.teacher'),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('date', models.DateField()),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.student')),
            ],
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.student'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.teacher'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(through='class.Enrollment', to='class.student'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ManyToManyField(through='class.Enrollment', to='class.teacher'),
        ),
    ]
