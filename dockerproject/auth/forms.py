from .models import CustomUser


class SignupForm:
    # age = forms.IntegerField()
    # weight = forms.IntegerField()

    class Meta:
        model = CustomUser

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.save()
        return user


class UserCreationForm:

    def __init__(self, *args, **kwargs):  # emailの登録を必須に変更
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    class Meta:
        model = get_user_model()
        fields = ["username", "email"]  # passwordは設定しない
        labels = {
            "username": "ユーザー名",
            "email": "メールアドレス",
        }
        help_texts = {
            "username": "",
            "email": "",
        }


class UserChangeForm:
    def __init__(self, *args, **kwargs):  # emailの登録を必須に変更
        super().__init__(*args, **kwargs)
        self.fields["email"].required = True

    class Meta:
        model = get_user_model()
        fields = ["username", "email"]  # passwordは設定しない
        labels = {
            "username": "ユーザー名",
            "email": "メールアドレス",
        }
        help_texts = {
            "username": "",
            "email": "",
        }
