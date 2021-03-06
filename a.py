# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DbBoard(models.Model):
    boardid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    write_date = models.DateTimeField()
    read_count = models.PositiveIntegerField()
    userid = models.ForeignKey('DbMember', models.DO_NOTHING)
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'db_board'


class DbGenre(models.Model):
    genreid = models.AutoField(primary_key=True)
    theme = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'db_genre'


class DbMember(models.Model):
    userid = models.CharField(primary_key=True, max_length=20)
    pwd = models.CharField(max_length=10)
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=13)
    checka = models.CharField(max_length=20)
    checkq = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'db_member'


class DbMovie(models.Model):
    movieid = models.AutoField(primary_key=True)
    poster = models.CharField(max_length=500)
    title = models.CharField(max_length=50)
    open_date = models.CharField(max_length=10)
    grade = models.IntegerField()
    running_time = models.IntegerField()
    director = models.CharField(max_length=30)
    actor = models.CharField(max_length=200)
    open_country = models.CharField(max_length=20)
    trailer = models.CharField(max_length=500, blank=True, null=True)
    summary = models.CharField(max_length=2000)
    genreid = models.ForeignKey(DbGenre, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'db_movie'


class DbReview(models.Model):
    reviewid = models.AutoField(primary_key=True)
    star = models.IntegerField()
    movieid = models.ForeignKey(DbMovie, models.DO_NOTHING, blank=True, null=True)
    userid = models.ForeignKey(DbMember, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'db_review'


class DbReviewVoter(models.Model):
    id = models.BigAutoField(primary_key=True)
    review = models.ForeignKey(DbReview, models.DO_NOTHING)
    member = models.ForeignKey(DbMember, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'db_review_voter'
        unique_together = (('review', 'member'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
