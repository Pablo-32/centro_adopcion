# Generated by Django 5.2.3 on 2025-06-25 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_adoptante_mascota_remove_adopter_adoption_history_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptante',
            name='gusta_raza',
            field=models.CharField(blank=True, choices=[('CCH', 'Caniche'), ('CH', 'Chihuahua'), ('LBR', 'Labrador'), ('PIT', 'Pitbull'), ('MIX', 'Mestizo')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(choices=[('CCH', 'Caniche'), ('CH', 'Chihuahua'), ('LBR', 'Labrador'), ('PIT', 'Pitbull'), ('MIX', 'Mestizo')], max_length=4),
        ),
    ]
