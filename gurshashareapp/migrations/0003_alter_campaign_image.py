# Generated by Django 4.2.2 on 2023-07-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gurshashareapp', '0002_campaign_image_alter_campaign_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]