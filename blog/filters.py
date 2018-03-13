import django_filters
import rest_framework_filters as filters
from django.core.validators import RegexValidator
from django.utils.encoding import force_text
from rest_framework import serializers

from .models import Post


class RestFrameworkRegexValidator(RegexValidator):

    def __call__(self, value):
        """
        Validate that the input contains a match for the regular expression
        if inverse_match is False, otherwise raise ValidationError.
        """
        if not (self.inverse_match is not bool(self.regex.search(
                force_text(value)))):
            raise serializers.ValidationError(self.message, code=self.code)


class PostFilter(filters.FilterSet):
    title = django_filters.CharFilter(
        name='title',
        lookup_expr='exact',
        validators=[
            RestFrameworkRegexValidator(
                regex='^[A-Z]$',
                message='Author format should be Adrian.',
                code='invalid_author',
            )],
        help_text='Full postalcode with format 1234AB.'
    )
    published_date = django_filters.DateTimeFilter(
        name='published_date',
        help_text='Housenumber with format ...',
        lookup_expr='exact'
    )
    published_date_min = django_filters.DateTimeFilter(
        name='published_date',
        lookup_expr='gte',
        help_text='Partial published_date of format ... Filters posts after this date.'
    )
    published_date_max = django_filters.DateTimeFilter(
        name='published_date',
        lookup_expr='lte',
        help_text='Partial published_date of format ... Filters posts before this date.'
    )

    class Meta:
        model = Post
        fields = [
            'author',
            'published_date',
            'published_date_min',
            'published_date_max',
        ]
