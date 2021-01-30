# Generated by Django 3.1.5 on 2021-01-30 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(default='')),
                ('fundador', models.CharField(max_length=50)),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('senha', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Perguntas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=250)),
                ('opcao_1', models.CharField(max_length=100)),
                ('opcao_2', models.CharField(max_length=100)),
                ('opcao_3', models.CharField(max_length=100)),
                ('correta', models.CharField(max_length=100)),
                ('pontuacao', models.IntegerField()),
                ('linguagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.linguagem')),
            ],
        ),
    ]
