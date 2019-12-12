# Generated by Django 2.2.8 on 2019-12-12 22:13

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ARContents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('image_contents', models.ImageField(upload_to='contents')),
                ('image_target', models.ImageField(help_text='JPG 파일만 사용해주세요.', upload_to='targets')),
                ('target_id', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'AR Content',
                'db_table': 'ar_contents',
            },
        ),
    ]
