class SearchActionMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            print('hi')
            queryset = queryset.filter(title__icontains=q, status="p")
        return queryset
