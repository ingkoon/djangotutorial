from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from quickstart.serializers import UserSerializer, GroupSerializer
<<<<<<< HEAD
from rest_framework.authentication import BasicAuthentication

=======
from django.http import JsonResponse, HttpResponse

# @api_view(['POST'])
>>>>>>> 179334d92776fb4e72d948c3618ec08da8ae3e76
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [BasicAuthentication]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return HttpResponse('postval')



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]