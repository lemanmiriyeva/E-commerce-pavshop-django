# Generated by Django 4.1.1 on 2022-11-20 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_time_stamp_replycomment_replied_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
        migrations.DeleteModel(
            name='ReplyComment',
        ),
    ]
