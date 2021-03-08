# お問い合わせのフォームを作成
# forms.pyは最初から用意されていないので自分で作成

from django import forms

class ContactForm(forms.Form):

    # 名前の入力フォーム

    name = forms.CharField(max_length=100, label='名前')

    # メールアドレスの入力フォーム

    email = forms.EmailField(max_length=100, label='メールアドレス')

    # メッセージの入力フォーム
    # 'widget=forms.Textarea()'を指定することで複数行のフォームになる

    message = forms.CharField(label='メッセージ', widget=forms.Textarea())