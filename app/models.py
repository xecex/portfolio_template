from django.db import models

# Profileモデルを作成

class Profile(models.Model):

    # 'null = True'、'blank = True'にするとURLが空白の場合はリンクが張られないように処理をしてくれる

    title = models.CharField('タイトル', max_length = 100, null = True, blank = True)
    subtitle = models.CharField('サブタイトル', max_length = 100, null = True, blank = True)
    name = models.CharField('名前', max_length = 100)
    job = models.TextField('仕事')
    introduction = models.TextField('自己紹介')
    github = models.CharField('github', max_length = 100, null = True, blank = True)
    twitter = models.CharField('twitter', max_length = 100, null = True, blank = True)
    linkedin = models.CharField('linkedin', max_length = 100, null = True, blank = True)
    facebook = models.CharField('facebook', max_length = 100, null = True, blank = True)
    instagram = models.CharField('instagram', max_length = 100, null = True, blank = True)

    # 'upload_to'は画像をアップロードするフォルダを指定する

    topimage = models.ImageField(upload_to = 'images', verbose_name = 'トップ画像')
    subimage = models.ImageField(upload_to = 'images', verbose_name = 'サブ画像')

    def __str__(self):
        return self.name

# ワークモデルの作成

class Work(models.Model):
    title = models.CharField('タイトル', max_length = 100)
    image = models.ImageField(upload_to = 'images', verbose_name = 'イメージ画像')
    thumbnail = models.ImageField(upload_to = 'images', verbose_name = 'サムネイル', null = True, blank = True)
    skill = models.CharField('スキル', max_length = 100)
    url = models.CharField('URL', max_length = 100, null = True, blank = True)
    created = models.DateField('作成日')
    description = models.TextField('説明')

    def __str__(self):
        return self.title

# 職歴モデルの作成

class Experience(models.Model):
    occupation = models.CharField('職種', max_length = 100)
    company = models.CharField('会社', max_length = 100)
    description = models.TextField('説明')
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.occupation

# 学歴モデルの作成

class Education(models.Model):
    course = models.CharField('コース', max_length=100)
    school = models.CharField('学校', max_length=100)
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.course

# ソフトウェアモデルの作成

class Software(models.Model):
    name = models.CharField('ソフトウェア', max_length=100)
    level = models.CharField('レベル', max_length=100)

    # 'IntegerField'を使用することで数字のみを扱うことができる

    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name

# テクニカルスキルモデルの作成

class Technical(models.Model):
    name = models.CharField('テクニカル', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name