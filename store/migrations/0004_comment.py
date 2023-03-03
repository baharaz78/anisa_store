# Generated by Django 4.1.7 on 2023-02-18 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='replies', to='store.comment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='store.product')),
            ],
        ),
    ]