# Generated by Django 4.1 on 2022-08-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogSlider',
            fields=[
                ('hslider_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='slideimage/')),
            ],
        ),
        migrations.CreateModel(
            name='contactSlider',
            fields=[
                ('hslider_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='slideimage/')),
            ],
        ),
        migrations.CreateModel(
            name='homeSliderOne',
            fields=[
                ('hslider_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=60, null=True)),
                ('ratings', models.CharField(max_length=60, null=True)),
                ('image', models.ImageField(upload_to='slideimage/')),
            ],
        ),
        migrations.CreateModel(
            name='homeSliderThree',
            fields=[
                ('hslider_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=60, null=True)),
                ('ratings', models.CharField(max_length=60, null=True)),
                ('image', models.ImageField(upload_to='slideimage/')),
            ],
        ),
        migrations.CreateModel(
            name='homeSliderTwo',
            fields=[
                ('hslider_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=60, null=True)),
                ('ratings', models.CharField(max_length=60, null=True)),
                ('image', models.ImageField(upload_to='slideimage/')),
            ],
        ),
        migrations.CreateModel(
            name='menuSlider',
            fields=[
                ('hslider_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='slideimage/')),
            ],
        ),
        migrations.CreateModel(
            name='storySlider',
            fields=[
                ('hslider_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='slideimage/')),
            ],
        ),
    ]
