from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django_app.models import App

# 別途作成したフォーム用のファイルを読み込む
from django_app.forms import AppForm


# Create your views here.
@login_required
def top(request):
    apps = App.objects.all().order_by("-created_at")  # 作成日時の降順でAppモデルのデータ取得
    context = {"apps": apps}
    # ここのrenderはtemplatesの中のファイルを探して読み込んでくれる。その時にpropsを渡すことができるので、そのpropsをhtml側で使うことができる。
    return render(request, "django_app/top.html", context)


# login_requiredデコレーターを使うことで、ログインしていないユーザーがこのページにアクセスした場合、ログインページにリダイレクトするようになります。
@login_required
def app_new(request):
    # POSTメソッドでリクエストが来た場合、フォームの内容を取得して、Appモデルに保存する。
    if request.method == "POST":
        form = AppForm(request.POST)
        # 登録するデータをここで検証する
        if form.is_valid():
            app = form.save(commit=False)
            # 登録する前に、ログインしているユーザーをcreated_byに設定する
            app.created_by = request.user
            app.save()
            # 新しい投稿ができたら、その投稿の詳細ページにリダイレクトする。
            return redirect(app_detail, app_id=app.pk)
    # GETメソッドでリクエストが来た場合、フォームを表示する。
    else:
        form = AppForm()
    return render(request, "django_app/app_new.html", {"form": form})


@login_required
def app_edit(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    # ログインしているユーザーと、投稿の作成者が一致しているかチェックする。
    if app.created_by_id != request.user.id:
        return HttpResponseForbidden("You are not authorized to edit this app.")

    if request.method == "POST":
        form = AppForm(request.POST, instance=app)
        if form.is_valid():
            app.save()
            return redirect(app_detail, app_id=app_id)
    else:
        form = AppForm(instance=app)
    return render(request, "django_app/app_edit.html", {"form": form})


def app_detail(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    return render(request, "django_app/app_detail.html", {"app": app})
