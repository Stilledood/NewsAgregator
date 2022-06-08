from django.shortcuts import render
from .models import Article,Comment
from django.views import View
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

class ArticleList(View):
    template_name='article_list.html'
    model=Article
    paginated_by=10
    page_kwargs='page'

    def get(self,request):
        article_list=self.model.objects.all()
        paginator=Paginator(article_list,self.paginated_by)
        page_number=request.GET(self.page_kwargs)
        try:
            page=paginator.page(page_number)
        except EmptyPage:
            page=paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            page=paginator.page(1)

        if page.has_previous():
            previous_page_url=f"?P{self.page_kwargs}={page.previous_page_number()}"
        else:
            previous_page_url=None

        if page.has_next():
            next_page_url=f"?P{self.page_kwargs}={page.next_page_number()}"
        else:
            next_page_url=None

        context={
            'article_list':page,
            'paginator':paginator,
            'next_page_url':next_page_url,
            'previous_page_url':previous_page_url
        }

        return render(request,self.template_name,context=context)

    


