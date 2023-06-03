from django.db import models


class Database(models.Model):
    name = models.CharField(verbose_name="名称", max_length=255)
    host = models.CharField(verbose_name="主机地址", max_length=255)
    user = models.CharField(verbose_name="用户", max_length=255)
    password = models.CharField(verbose_name="密码", max_length=255)
    port = models.IntegerField(verbose_name="端口", default=3306)
    desc = models.CharField(verbose_name="备注", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "数据库信息"
        verbose_name_plural = verbose_name
        db_table = "devops_databases"


