from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import View
from .forms import ContactForm
from .models import Profile, Work, Experience, Education, Software, Technical
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap

class IndexView(View):
    def get(self, request, *args, **kwargs):

        # 全てのプロフィールデータを取得

        profile_data = Profile.objects.all()

        # もしプロフィールデータが存在したら、最新のプロフィールデータを降順にして取得

        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]

        # トップページに作品リストを表示（降順に並べ替え）

        work_data = Work.objects.order_by('-id')

        # プロフィールデータ、作品データをindex.htmlに渡す

        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'work_data': work_data
        })

class DetailView(View):
    def get(self, request, *args, **kwargs):

        # urlから取得したidを使ってワークデータを取得

        work_data = Work.objects.get(id = self.kwargs['pk'])

        # ワークデータをdetail.htmlに渡す

        return render(request, 'app/detail.html', {
            'work_data': work_data
        })

# プロフィール用のクラスを作成

class AboutView(View):
    def get(self, request, *args, **kwargs):

        # プロフィールデータを全て取得

        profile_data = Profile.objects.all()

        # プロフィールデータが存在する場合

        if profile_data.exists():

            # 最新のプロフィールデータを取得

            profile_data = profile_data.order_by('-id')[0]

        # 最新の各データを取得

        experience_data = Experience.objects.order_by('-id')
        education_data = Education.objects.order_by('-id')
        software_data = Software.objects.order_by('-id')
        technical_data = Technical.objects.order_by('-id')
        return render(request, 'app/about.html', {

            # 各データをテンプレートに渡す

            'profile_data': profile_data,
            'experience_data': experience_data,
            'education_data': education_data,
            'software_data': software_data,
            'technical_data': technical_data
        })

# お問い合わせ用のクラスを作成

class ContactView(View):
    def get(self, request, *args, **kwargs):

        # forms.pyで定義したフォームをコールします

        form = ContactForm(request.POST or None)

        # フォーム情報をテンプレートに渡す

        return render(request, 'app/contact.html', {
            'form': form
        })

    # postとgetはブラウザがサーバーにリクエストを送る時に使えるメソッドの種類
    # リクエストを送ると一緒にメソッドの情報も送られる
    # リクエストはDjangoに送られ、Djangoの中でメソッドに応じた処理が行われる
    # getは、ページが表示された時にコールされる関数
    # postは、何かの情報をサーバーに送るときにコールされる関数

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        # フォームの内容が正しいかどうかを判断

        if form.is_valid():

            # フォームから入力したname、email、messageの取得

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # 件名の設定

            subject = 'お問い合わせありがとうございます。'

            # メール内容の設定
            # 'textwrap.dedent'関数を使用すると共通で現れる先頭の空白を削除してくれる（便利なテクニック）

            contact = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。

                {name} 様

                お問い合わせありがとうございました。
                以下の内容でお問い合わせを受付いたしました。
                内容を確認させていただき、ご返信させていただきますので少々お待ちください。

                ---------------------
                ■お名前
                {name}

                ■メールアドレス
                {email}

                ■メッセージ
                {message}
                ---------------------
                ''').format(

                # '.format'で変数を内容に組み込むことができる

                    name = name,
                    email = email,
                    message = message
                )
            to_list = [email]

            # 自分のメールアドレスがbccに設定される
            # お問い合わせがあると自分のメールにも通知が行くようになる

            bcc_list = [settings.EMAIL_HOST_USER]

            # 送信処理

            try:
                message = EmailMessage(subject=subject, body=contact, to = to_list, bcc = bcc_list)
                message.send()

            # 無効な送信があった場合の処理

            except BadHeaderError:
                return HttpResponse('無効なヘッダが検出されました。')

            return redirect('thanks')

        # フォーム内容に不備があった場合、空のフォーム画面が表示される

        return render(request, 'app/contact.html', {
            'form': form
        })

# お問い合わせ完了用のクラスを作成

class ThanksView(View):
    def get(self, request, *args, **kwargs):

        # お問い合わせ完了画面に遷移するように設定

        return render(request, 'app/thanks.html')