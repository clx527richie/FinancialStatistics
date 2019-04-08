# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MsreplicationObjects(models.Model):
    publisher = models.CharField(max_length=128, blank=True, null=True)
    publisher_db = models.CharField(max_length=128, blank=True, null=True)
    publication = models.CharField(max_length=128, blank=True, null=True)
    object_name = models.CharField(max_length=128)
    object_type = models.CharField(max_length=2)
    article = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSreplication_objects'


class MsreplicationSubscriptions(models.Model):
    publisher = models.CharField(max_length=128)
    publisher_db = models.CharField(max_length=128, blank=True, null=True)
    publication = models.CharField(max_length=128, blank=True, null=True)
    independent_agent = models.BooleanField()
    subscription_type = models.IntegerField()
    distribution_agent = models.CharField(max_length=128, blank=True, null=True)
    time = models.DateTimeField()
    description = models.CharField(max_length=255, blank=True, null=True)
    transaction_timestamp = models.BinaryField()
    update_mode = models.SmallIntegerField()
    agent_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    subscription_guid = models.TextField(blank=True, null=True)  # This field type is a guess.
    subid = models.TextField(blank=True, null=True)  # This field type is a guess.
    immediate_sync = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'MSreplication_subscriptions'
        unique_together = (('publisher', 'publisher_db', 'publication', 'subscription_type', 'transaction_timestamp'),)


class Mssavedforeignkeycolumns(models.Model):

    class Meta:
        managed = False
        db_table = 'MSsavedforeignkeycolumns'


class Mssavedforeignkeyextendedproperties(models.Model):
    program_name = models.CharField(max_length=128)
    constraint_name = models.CharField(max_length=128)
    parent_schema = models.CharField(max_length=128)
    property_name = models.CharField(max_length=128)
    property_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'MSsavedforeignkeyextendedproperties'


class Mssavedforeignkeys(models.Model):
    program_name = models.CharField(max_length=128)
    constraint_name = models.CharField(max_length=128)
    parent_schema = models.CharField(max_length=128)
    parent_name = models.CharField(max_length=128)
    referenced_object_schema = models.CharField(max_length=128)
    referenced_object_name = models.CharField(max_length=128)
    is_disabled = models.BooleanField()
    is_not_for_replication = models.BooleanField()
    is_not_trusted = models.BooleanField()
    delete_referential_action = models.SmallIntegerField()
    update_referential_action = models.SmallIntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'MSsavedforeignkeys'


class Mssnapshotdeliveryprogress(models.Model):
    session_token = models.CharField(max_length=260)
    progress_token_hash = models.IntegerField()
    progress_token = models.CharField(max_length=500)
    progress_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSsnapshotdeliveryprogress'


class MssubscriptionAgents(models.Model):
    id = models.AutoField()
    publisher = models.CharField(max_length=128)
    publisher_db = models.CharField(max_length=128)
    publication = models.CharField(max_length=128)
    subscription_type = models.IntegerField()
    queue_id = models.CharField(max_length=128, blank=True, null=True)
    update_mode = models.SmallIntegerField()
    failover_mode = models.BooleanField()
    spid = models.IntegerField()
    login_time = models.DateTimeField()
    allow_subscription_copy = models.BooleanField()
    attach_state = models.IntegerField()
    attach_version = models.TextField()  # This field type is a guess.
    last_sync_status = models.IntegerField(blank=True, null=True)
    last_sync_summary = models.CharField(max_length=128, blank=True, null=True)
    last_sync_time = models.DateTimeField(blank=True, null=True)
    queue_server = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MSsubscription_agents'
        unique_together = (('publisher', 'publisher_db', 'publication', 'subscription_type'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):

    class Meta:
        managed = False
        db_table = 'django_session'


class LisAdmin(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_admin'


class LisBuy(models.Model):
    buy_id = models.AutoField(primary_key=True)
    buy_name = models.CharField(max_length=50, blank=True, null=True)
    buy_price = models.CharField(max_length=50, blank=True, null=True)
    buy_priceyj = models.CharField(max_length=50, blank=True, null=True)
    buy_tips = models.CharField(max_length=50, blank=True, null=True)
    buy_time = models.DateTimeField(blank=True, null=True)
    hospitalcode = models.CharField(max_length=50, blank=True, null=True)
    pat_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    idcard = models.CharField(max_length=50, blank=True, null=True)
    pat_phone = models.CharField(max_length=50, blank=True, null=True)
    pat_agestr = models.CharField(max_length=50, blank=True, null=True)
    yishengzhenduan = models.TextField(blank=True, null=True)  # This field type is a guess.
    dengdancode = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    bd = models.CharField(max_length=10, blank=True, null=True)
    barhead = models.CharField(max_length=50, blank=True, null=True)
    barbody = models.CharField(max_length=50, blank=True, null=True)
    req_itemcode = models.CharField(max_length=50, blank=True, null=True)
    itemstat = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_buy'


class LisBuyBak(models.Model):
    buy_id = models.AutoField(primary_key=True)
    buy_name = models.CharField(max_length=50, blank=True, null=True)
    buy_price = models.CharField(max_length=50, blank=True, null=True)
    buy_priceyj = models.CharField(max_length=50, blank=True, null=True)
    buy_tips = models.CharField(max_length=50, blank=True, null=True)
    buy_time = models.DateTimeField(blank=True, null=True)
    hospitalcode = models.CharField(max_length=50, blank=True, null=True)
    pat_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    idcard = models.CharField(max_length=50, blank=True, null=True)
    pat_phone = models.CharField(max_length=50, blank=True, null=True)
    pat_agestr = models.CharField(max_length=50, blank=True, null=True)
    dengdancode = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    bd = models.CharField(max_length=10, blank=True, null=True)
    barhead = models.CharField(max_length=50, blank=True, null=True)
    barbody = models.CharField(max_length=50, blank=True, null=True)
    req_itemcode = models.CharField(max_length=50, blank=True, null=True)
    xmzt = models.CharField(max_length=50, blank=True, null=True)
    itemstat = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_buy_bak'


class LisBuysave(models.Model):
    buy_saveid = models.IntegerField(blank=True, null=True)
    pat_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    idcard = models.CharField(max_length=50, blank=True, null=True)
    pat_phone = models.CharField(max_length=50, blank=True, null=True)
    pat_agestr = models.CharField(max_length=50, blank=True, null=True)
    sum = models.CharField(max_length=50, blank=True, null=True)
    fuwufei = models.CharField(max_length=50, blank=True, null=True)
    sum1 = models.CharField(max_length=50, blank=True, null=True)
    dengdancode = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    paystat = models.CharField(max_length=50, blank=True, null=True)
    hospitalcode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_buysave'


class LisBuysaveBak(models.Model):
    buy_saveid = models.IntegerField(blank=True, null=True)
    pat_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    idcard = models.CharField(max_length=50, blank=True, null=True)
    pat_phone = models.CharField(max_length=50, blank=True, null=True)
    pat_agestr = models.CharField(max_length=50, blank=True, null=True)
    sum = models.CharField(max_length=50, blank=True, null=True)
    fuwufei = models.CharField(max_length=50, blank=True, null=True)
    sum1 = models.CharField(max_length=50, blank=True, null=True)
    dengdancode = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    paystat = models.CharField(max_length=50, blank=True, null=True)
    hospitalcode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_buysave_bak'


class LisCaiwu(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_caiwu'


class LisChongzhiguanli(models.Model):
    chongzhiid = models.AutoField()
    chongzhi_xishu = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_chongzhiguanli'


class LisCjjbClass(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_cjjb_class'


class LisCjjbClassXm(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_cjjb_class_xm'


class LisDaili(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_daili'


class LisDingdanstat(models.Model):
    stat_id = models.AutoField(primary_key=True)
    dengdancode = models.CharField(max_length=50, blank=True, null=True)
    pat_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    pat_phone = models.CharField(max_length=50, blank=True, null=True)
    pat_agestr = models.CharField(max_length=50, blank=True, null=True)
    idcard = models.CharField(max_length=50, blank=True, null=True)
    yishengzhenduan = models.TextField(blank=True, null=True)
    hospitalcode = models.CharField(max_length=50, blank=True, null=True)
    sum = models.CharField(max_length=50, blank=True, null=True)
    sum1 = models.CharField(max_length=50, blank=True, null=True)
    pay_stat = models.CharField(max_length=10, blank=True, null=True)
    tijiao_time = models.DateTimeField(blank=True, null=True)
    bd_stat = models.CharField(max_length=10, blank=True, null=True)
    jy = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_dingdanstat'


class LisFuwufei(models.Model):
    fuwufeiid = models.AutoField()
    fuwufei_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_fuwufei'


class LisGuanli(models.Model):
    guanli_id = models.AutoField()
    guanli_name = models.CharField(max_length=50, blank=True, null=True)
    guanli_pass = models.CharField(max_length=50, blank=True, null=True)
    guanli_quanxian = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_guanli'


class LisItem(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_item'


class LisItemBak(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_item_bak'


class LisJianyan(models.Model):
    jianyan_id = models.AutoField()
    jianyanname = models.CharField(max_length=50, blank=True, null=True)
    jianyanpass = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_jianyan'


class LisJifen(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_jifen'


class LisJifenShengyu(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_jifen_shengyu'


class LisJifenZhifu(models.Model):
    zhifu_id = models.AutoField()
    dengdancode = models.CharField(max_length=50, blank=True, null=True)
    buy_price = models.CharField(max_length=50, blank=True, null=True)
    buy_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_jifen_zhifu'


class LisJyxmClass(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_jyxm_class'


class LisJyxmClassXm(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_jyxm_class_xm'


class LisQuanxian(models.Model):
    quanxian_id = models.AutoField()
    quanxian_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_quanxian'


class LisTuifei(models.Model):
    tuifei_id = models.AutoField()
    item_id = models.CharField(max_length=50, blank=True, null=True)
    dengdancode = models.CharField(max_length=50, blank=True, null=True)
    buy_name = models.CharField(max_length=50, blank=True, null=True)
    req_itemcode = models.CharField(max_length=50, blank=True, null=True)
    buy_price = models.CharField(max_length=50, blank=True, null=True)
    buy_priceyj = models.CharField(max_length=50, blank=True, null=True)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    buy_tips = models.CharField(max_length=50, blank=True, null=True)
    pat_name = models.CharField(max_length=50, blank=True, null=True)
    pat_phone = models.CharField(max_length=50, blank=True, null=True)
    pat_sex = models.CharField(max_length=50, blank=True, null=True)
    pat_idcard = models.CharField(max_length=50, blank=True, null=True)
    pat_agestr = models.CharField(max_length=50, blank=True, null=True)
    jiaoyistat = models.CharField(max_length=50, blank=True, null=True)
    zhifu_time = models.DateTimeField(blank=True, null=True)
    mz_shenqingtime = models.DateTimeField(blank=True, null=True)
    neiqin_shenqingtime = models.DateTimeField(blank=True, null=True)
    mz_shenqingzhuangtai = models.CharField(max_length=10, blank=True, null=True)
    neiqin_shenqingzhuangtai = models.CharField(max_length=10, blank=True, null=True)
    caiwu_chulizhuangtai = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_tuifei'


class LisTuifeiguanli(models.Model):
    tuifeiguanli_id = models.AutoField()
    tuifeiguanli_name = models.CharField(max_length=50, blank=True, null=True)
    tuifeiguanli_pass = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_tuifeiguanli'


class LisWuliu(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_wuliu'


class LisXian(models.Model):

    class Meta:
        managed = False
        db_table = 'lis_xian'


class LisXiangmuClassXq(models.Model):
    xiangmuclassid = models.CharField(max_length=50, blank=True, null=True)
    itemid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lis_xiangmu_class_xq'


class RecordJifenzhifu(models.Model):

    class Meta:
        managed = False
        db_table = 'record_jifenzhifu'


class RegHospitemdiscount(models.Model):
    discountid = models.IntegerField(primary_key=True)
    req_itemcode = models.CharField(max_length=32)
    discount = models.DecimalField(max_digits=8, decimal_places=4)
    disprice = models.DecimalField(max_digits=12, decimal_places=4)
    saleman = models.CharField(max_length=20, blank=True, null=True)
    req_itemprice = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    operateuser = models.CharField(max_length=64, blank=True, null=True)
    operatedt = models.DateTimeField(blank=True, null=True)
    pediscount = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    pedisprice = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    emerdiscount = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    emerdisprice = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg_hospitemdiscount'
        unique_together = (('discountid', 'req_itemcode'),)


class ReqItemDict(models.Model):

    class Meta:
        managed = False
        db_table = 'req_item_dict'


class ReqItemDict2(models.Model):

    class Meta:
        managed = False
        db_table = 'req_item_dict2'


class SysUser(models.Model):

    class Meta:
        managed = False
        db_table = 'sys_user'
