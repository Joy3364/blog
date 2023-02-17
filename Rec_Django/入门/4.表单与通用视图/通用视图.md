## 目的
**视图函数**接受request请求与Url参数，返回渲染后的html文件  
一些模板的**局部结构**可能是高度**相似**的，例如歌单，书单，菜单等等，   
**模板继承**可以将这些**局部结构独立**出来，  
**通用视图**主要用于传递模板上下文，   
上下文传递不外乎：单表全传，单表传部分，单/部分表附加一些其他，  
通用视图提供了这些操作的**快捷方式**  
二者结合与**模板继承**结合起来，简化开发流程。
## 使用方法
as_view()
## 构建通用视图（基于不同的传递方法）
```python
### 内置属性
model       # 指定 主要模型
queryset    # 存放 主要数据表，若不指定，主要数据表 将为 主要模型 的 全部
context_object_name # 指定 主要数据表 的 名称，默认为 object_list

### 内置方法
get_queryset        # 默认情况下，若 queryset 被设置，则返回 queryset，否则， 返回 model 的 全部
                    # 若被重写，返回自定义数据
get_context_data    # 返回 全部上下文（字典）， 包括 主要数据表 和 其他上下文

# 1. 单表全传
from django.views.generic import ListView
from books.models import Publisher

class PublisherListView(ListView):
    template_name = "dsdnh.html" # 指定子模版，否则会根据模型自动推测
    context_object_name = "" # 指定子模版上下文名称，默认为object_list
    model = Publisher # 默认全传

# 2. 单表附加其他 需要调用父方法
from django.views.generic import DetailView
from books.models import Book, Publisher

class PublisherDetailView(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

# 3. 通过 queryset 过滤数据表
from django.views.generic import DetailView
from books.models import Publisher

class PublisherDetailView(DetailView):

    context_object_name = 'publisher'
    queryset = Publisher.objects.all()[:4]

# 4. 通过重载函数过滤数据表
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from books.models import Book, Publisher

class PublisherBookListView(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)
```
