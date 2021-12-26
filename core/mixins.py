class SearchActionMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        # only show published ones.
        queryset = queryset.filter(status="p")
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset
