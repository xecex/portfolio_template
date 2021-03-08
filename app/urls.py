# アプリケーション用のurls.pyは最初から用意されていないため、appフォルダの下に作成

from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),

    # <int:pk>とすることでワークデータのidをurlに表示することができ、どの作品の詳細画面なのかを判断できる

    path('detail/<int:pk>', views.DetailView.as_view(), name = 'detail'),

    # プロフィール用のurl

    path('about/', views.AboutView.as_view(), name = 'about'),

    # お問い合わせ用のurl

    path('contact/', views.ContactView.as_view(), name = 'contact'),

    path('thanks/', views.ThanksView.as_view(), name = 'thanks'),
]
