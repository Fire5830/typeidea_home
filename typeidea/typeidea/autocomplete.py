from dal import autocomplete

from blog.models import Category, Tags


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Category.objects.none()

        qs = Category.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class TagsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Tags.objects.none()

        qs = Tags.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

