from django.db import models


class BaseModel(models.Model):
    # 通用字段
    created_by = models.CharField(verbose_name="创建人", max_length=128, null=True, blank=True)
    updated_by = models.CharField(verbose_name="更新人", max_length=128, null=True, blank=True)
    date_created = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    desc = models.CharField(verbose_name="备注", max_length=255, null=True, blank=True)



class AssetsCategory(BaseModel):
    """
        资产分类
    """
    name = models.CharField(verbose_name="分类名称", max_length=128)
    parent_category = models.ForeignKey("self", verbose_name="父分类", null=True, blank=True,
                                        on_delete=models.SET_NULL, related_name="sub_cat")

    def __str__(self):
        return "{}-{}".format(self.parent_category, self.name)

    class Meta:
        verbose_name = "资产分类"
        verbose_name_plural = verbose_name
        db_table = "devops_category"


class Assets(BaseModel):
    """
        资产 Model
    """
    name = models.CharField(verbose_name="主机名称", max_length=128)
    address = models.CharField(verbose_name="主机地址", max_length=255, db_index=True)
    is_active = models.BooleanField(verbose_name="激活状态", default=True)
    assets_category = models.ForeignKey(AssetsCategory, verbose_name="资产分类", null=True, blank=True,
                                        on_delete=models.SET_NULL)

    def __str__(self):
        return "{0.name}({0.address})".format(self)

    class Meta:
        verbose_name = "资产信息"
        verbose_name_plural = verbose_name
        db_table = "devops_assets"

