# Generated by Django 4.2.2 on 2023-07-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurshashareapp', '0003_alter_campaign_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='recipent',
            field=models.CharField(blank=True, choices=[('Yourself', 'Yourself'), ('Someone else', 'Someone else'), ('Charity', 'Charity')], max_length=100, null=True),
        ),
    ]