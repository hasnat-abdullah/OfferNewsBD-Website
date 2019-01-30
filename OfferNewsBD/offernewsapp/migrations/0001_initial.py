# Generated by Django 2.1.2 on 2019-01-28 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durationType', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durationType', models.CharField(max_length=20)),
                ('adExpireDate', models.DateField()),
                ('adDate', models.DateField(auto_now_add=True)),
                ('isActive', models.BooleanField(default=True)),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.AdPricing')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchName', models.CharField(max_length=20)),
                ('branchAddress', models.TextField(max_length=200)),
                ('branchPhn', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=20)),
                ('catIcon', models.FileField(blank=True, default='default.jpg', upload_to='cat_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comName', models.CharField(db_index=True, max_length=60)),
                ('comDes', models.TextField()),
                ('comAddress', models.TextField(max_length=200)),
                ('comPhn', models.CharField(max_length=11)),
                ('comWeb', models.CharField(blank=True, max_length=42)),
                ('comImage', models.ImageField(blank=True, default='default.jpg', upload_to='com_pics')),
                ('infoUpdatedOn', models.DateField(auto_now=True)),
                ('createdOn', models.DateField(auto_now_add=True)),
                ('isVerified', models.BooleanField()),
                ('AuthorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phn', models.CharField(db_index=True, default=1, max_length=11)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=250)),
                ('sendOn', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couponCode', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featuredType', models.CharField(choices=[('FP', 'Feature_Post'), ('FC', 'Feature_Company')], default='FP', max_length=2)),
                ('featuredExpireDate', models.DateField()),
                ('featuredDate', models.DateField(auto_now_add=True)),
                ('isActive', models.BooleanField(db_index=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('C', 'Cover'), ('F', 'First_Page'), ('P', 'Popup')], default='F', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturePricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durationType', models.CharField(max_length=20)),
                ('featuredType', models.CharField(choices=[('FP', 'Feature_Post'), ('FC', 'Feature_Company')], default='FP', max_length=2)),
                ('priceAmount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keyword', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('description', models.TextField()),
                ('offerType', models.CharField(choices=[('D', 'Deal'), ('C', 'Coupon')], default='D', max_length=1)),
                ('AmountType', models.CharField(choices=[('P', 'Percentage'), ('T', 'Taka'), ('G', 'Gift')], default='P', max_length=1)),
                ('Amount', models.CharField(max_length=200)),
                ('postImage', models.ImageField(blank=True, default='default.jpg', upload_to='post_pics')),
                ('isActive', models.BooleanField(default=True)),
                ('isFeatured', models.BooleanField(default=False)),
                ('goingUrl', models.URLField()),
                ('postedOn', models.DateTimeField(auto_now_add=True)),
                ('expiredOn', models.DateTimeField()),
                ('editedOn', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Category')),
                ('comName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phn', models.CharField(db_index=True, max_length=11, unique=True)),
                ('infoUpdatedOn', models.DateField(auto_now=True)),
                ('createdOn', models.DateField(auto_now_add=True)),
                ('userPic', models.ImageField(blank=True, default='default', upload_to='pro_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='featured',
            name='postId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Post'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='postId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Post'),
        ),
        migrations.AddField(
            model_name='branch',
            name='comId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offernewsapp.Company'),
        ),
        migrations.AddField(
            model_name='branch',
            name='managerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]