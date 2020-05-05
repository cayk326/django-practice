from django.db import models

from django.core import validators

# Create Model Item
class Item(models.Model):
  
  # Create Item model's property
  SEX_CHOICES = (
    (1, '男性'),
    (2, '女性'),
  )


  name = models.CharField(
    verbose_name='名前',
    max_length=200,
  )

  #バリデーションとは、入力された値が正しいかどうかチェックする。
  age = models.IntegerField(
    verbose_name='年齢',
    validators=[validators.MinValueValidator(1)],#最大値が1
    blank=True,
    null=True,
    )

  sex = models.IntegerField(
    verbose_name='性別',
    choices=SEX_CHOICES,
    default=1
    )
  memo = models.TextField(
    verbose_name='備考',
    max_length=300,
    blank=True,
    null=True,
    )
  created_at = models.DateTimeField(
    verbose_name='登録日',
    auto_now_add=True
  )

  # 以下は管理サイト上の表示設定
  def __str__(self):
    return self.name
  # メタクラスを定義することで、このクラスが何をするものなのかを定義する。
  class Meta:
    verbose_name = 'アイテム'
    verbose_name_plural = 'アイテム'


