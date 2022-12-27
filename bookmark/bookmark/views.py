from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']  # 어떤 필드들을 입력받을 것인지
    success_url = reverse_lazy('list')  # 글쓰기를 완료하고 이동할 페이지
    template_name_suffix = '_create'  # 사용할 템플릿의 접미사만 변경하는 설정값
