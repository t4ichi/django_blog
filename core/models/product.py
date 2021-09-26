from django.db import models
from django.conf import settings

import uuid
import os

def upload_image_path(instance, filename):
    """ 商品画像を保存するパスを返す """
    item_id = str(instance.id)
    return os.path.join(settings.PRODUCT_IMAGES_DIR, item_id, filename)


def create_noneimage_path() -> str:
    """ 商品画像が存在しない事を表す、NoImage画像のパスを返す """
    return os.path.join(settings.PRODUCT_IMAGES_DIR, 'no_image.png')


def get_or_create_category_initial_record():
    """
        カテゴリモデルに'全て'というレコードを登録して、登録した値を返す。登録済みの場合登録せず値のみ返す。
        FIXME: ProductModelのcategoryをNull許容にしたくないので、これが必要だが、もっと良いやり方がありそうな気がする。引数が取れないので、同じことをしたいカラムが増えると冗長になる。
    """
    return CategoryModel.objects.get_or_create(name='全て')


def get_or_create_tag_initial_record():
    """
        タグモデルに'全て'というレコードを登録して、登録した値を返す。登録済みの場合登録せず値のみ返す。
        FIXME: ProductModelのtagsをNull許容にしたくないので、これが必要だが、もっと良いやり方がありそうな気がする。引数が取れないので、同じことをしたいカラムが増えると冗長になる。
    """
    return TagModel.objects.get_or_create(name='全て')


class CategoryModel(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class TagModel(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class MakerModel(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(verbose_name='商品名', max_length=50)
    maker = models.ForeignKey(MakerModel, verbose_name='メーカー', on_delete=models.PROTECT)
    description = models.TextField(verbose_name='商品説明')
    price = models.IntegerField(verbose_name='価格')
    stock = models.IntegerField(verbose_name='在庫', default=0)
    sales_figures = models.IntegerField(verbose_name='販売数', default=0)
    image_path = models.ImageField(verbose_name='商品画像', upload_to=upload_image_path, default=create_noneimage_path)
    is_published = models.BooleanField(verbose_name='公開', default=False)
    model_year = models.IntegerField(verbose_name='年式', default='',)
    category = models.ForeignKey(CategoryModel, verbose_name='カテゴリ', on_delete=models.PROTECT, default=get_or_create_category_initial_record)
    tags = models.ManyToManyField(TagModel, verbose_name='タグ', default=get_or_create_tag_initial_record)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '商品情報'
