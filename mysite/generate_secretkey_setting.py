# 最初にプロジェクトをgit cloneしたときにSECRET_KEYを生成するスクリプトの設定

from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
text = 'SECRET_KEY = \'{0}\''.format(secret_key)
print(text)