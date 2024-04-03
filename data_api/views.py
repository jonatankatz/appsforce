from django.db.models import Count
from django.http import JsonResponse
from .models import User, Department
from rest_framework import generics,filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import UserSerializer, DepartmentSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DepartmentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    partial = True

class DepartmentDeleteView(generics.DestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete department"))


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    partial = True

# implementing users read with filters
class AllUserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['first_name','last_name','email','department']
    search_fields = ['first_name', 'last_name','email','department__name']




class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete user"))



def get_departments_with_counts(request):
    # added id to values to ensure group by works correctly
    # since name isn't unique
    departments = Department.objects \
        .values("id","name","description") \
        .annotate(usersCount=Count('user'))

    output_json = []
    # we could also just convert to list and remove id key
    for department in departments:
        output_json.append({
            "name": department["name"],
            "description": department["description"],
            "usersCount": department["usersCount"]
        })

    # django by default doesn't allow you to return a non-dict json response
    return JsonResponse(output_json, safe=False)    