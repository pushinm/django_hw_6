# Generated by Django 4.1.5 on 2023-01-27 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ice_cream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Мороженное')),
                ('taste', models.CharField(choices=[('Шоколад', 'Шоколад'), ('Клубника', 'Клубника'), ('Ваниль', 'Ваниль')], max_length=100, verbose_name='Вкус')),
            ],
            options={
                'verbose_name': 'Мороженное',
                'verbose_name_plural': 'Мороженные',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ice_market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название киоска')),
                ('ice_cream', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ice_creams.ice_cream')),
            ],
            options={
                'verbose_name': 'Киоск',
                'verbose_name_plural': 'Киоски',
                'ordering': ['name'],
            },
        ),
    ]