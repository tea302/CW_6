import django_filters

from .models import Mymodel


class MyModelFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )

    class Meta:
        model = Mymodel
        fields = ("title",)
