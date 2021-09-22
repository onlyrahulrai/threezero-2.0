# Generated by Django 3.2.7 on 2021-09-22 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_social_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social', to='authentication.profile'),
        ),
    ]
