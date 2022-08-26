# Generated by Django 3.2.9 on 2022-08-26 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
        ('template', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(help_text='项目域名', max_length=125)),
                ('remote_addr', models.CharField(help_text='远程请求地址', max_length=64)),
                ('uri', models.CharField(blank=True, help_text='请求路径', max_length=125, null=True)),
                ('header', models.CharField(blank=True, help_text='请求头', max_length=1024, null=True)),
                ('content', models.TextField(blank=True, help_text='接收内容', null=True)),
                ('message_type', models.IntegerField(choices=[(1, 'http'), (2, 'dns'), (3, 'ldap'), (4, 'rmi')], default=1, help_text='消息类型')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True)),
                ('task', models.ForeignKey(db_constraint=False, default='', help_text='所属任务', on_delete=django.db.models.deletion.CASCADE, related_name='task_message', to='task.task')),
                ('template', models.ForeignKey(db_constraint=False, default=1, help_text='所属组件', on_delete=django.db.models.deletion.CASCADE, related_name='template_message', to='template.template')),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]
