# Generated by Django 3.0.14 on 2021-08-18 08:19

import core.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_users'),
        ('medical_pricelist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesPricelistMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='services_pricelists', to='core.MutationLog')),
                ('pricelist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='medical_pricelist.ServicesPricelist')),
            ],
            options={
                'db_table': 'medical_ServicesPricelistMutation',
                'managed': True,
            },
            bases=(models.Model, core.models.ObjectMutation),
        ),
        migrations.CreateModel(
            name='ItemsPricelistMutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mutation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='items_pricelists', to='core.MutationLog')),
                ('pricelist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mutations', to='medical_pricelist.ItemsPricelist')),
            ],
            options={
                'db_table': 'medical_ItemsPricelistMutation',
                'managed': True,
            },
            bases=(models.Model, core.models.ObjectMutation),
        ),
    ]
