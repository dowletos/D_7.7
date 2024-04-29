from django_filters import FilterSet,ModelChoiceFilter,CharFilter,DateTimeFilter
from .models import  *



class ProductFilter(FilterSet):


    F_author_name_ = ModelChoiceFilter(field_name='author_ID_FK__user__username',queryset=User.objects.all(),empty_label='---Любое----',label="По имени автора:")
    F_header__=CharFilter(field_name='post_title', lookup_expr='icontains',label='По названию:')
    F_date_created=DateTimeFilter(field_name='date_and_time_created',widget= forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), lookup_expr='gte',label='Позже Даты (ГГГГ-ММ-ДД):')

    class Meta:
        model=Post
        fields=[]
