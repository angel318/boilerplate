# from . import utils
from rest_framework.views import Response, APIView
from . import models
from . import serializers
from rest_framework import viewsets, status, exceptions, permissions
from project.common.pagination import PageNumberPagination
from django.conf import settings

# class ItemsView(APIView):
#
#     permission_classes = (permissions.IsAuthenticated, )
#
#     def get(self, request, exampleid):
#         # Start pagination instance class
#         paginator = PageNumberPagination()
#         objects = models.Project.objects.get(
#             pk=exampleid
#         ).items.filter(
#             status=1
#         )
#         # Result page
#         result_page = paginator.paginate_queryset(objects, request)
#         # Serialize objects
#         serializer = wserializers.ItemsSerializer(result_page, many=True)
#
#         return paginator.get_paginated_response(serializer.data)


class ObjectViewSet(viewsets.ModelViewSet):
    model = models.Object
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.ObjectSerializer

    def get_queryset(self):
        kwargs = self.request.GET
        name = kwargs.get('name', None)

        queryset = self.model.objects.all()

        queryset = queryset.filter(
            # owner=self.request.user,
            is_active=True
        )

        if name:
            queryset = queryset.filter(
                name__icontains=name
            )

        print(settings.AWS_ENABLE)
        print(type(settings.AWS_ENABLE))
        if settings.AWS_ENABLE:
            print('Enabled S3')
        else:
            print('not enabled S3')

        return queryset

    def perform_create(self, serializer):

        item = serializer.save(
            owner=self.request.user,
            is_active=True
        )
        return item

    def perform_update(self, serializer):

        return serializer.save()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        # print(instance)
