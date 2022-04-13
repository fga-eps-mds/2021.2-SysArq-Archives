# Generated by Django 3.2.6 on 2022-04-13 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives_app', '0005_auto_20220412_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxarchiving',
            name='unity_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='unfiled_unity_box', to='archives_app.unity'),
        ),
    ]
