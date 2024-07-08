from django.views.generic import TemplateView

class CollectionIndexView(TemplateView):
    template_name = 'collection_list.html'