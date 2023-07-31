from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import Place
from .serializers import placesSerializer
from django.db import connections

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class placeView(APIView):
    # pagination_class = PageNumberPagination
    

    def get(self, request):
        queryset = '''select * from Place'''  # Replace with your queryset
        # paginator = self.pagination_class()
        # paginated_queryset = paginator.paginate_queryset(queryset, request)
        # serializer = placesSerializer(paginated_queryset, many=True)  # Replace with your serializer
        
        with connections['warehouse'].cursor() as cursor:
            cursor.execute(queryset)
            places_data = dictfetchall(cursor)
        
            print(places_data)
        return Response(places_data)
    
    def post(self, request):
        serializer = placesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






