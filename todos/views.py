from rest_framework import status,serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


class TodoView(APIView):
    # create - post
    def post(self,request):
        try:
            serializers = TodoSerializer(data = request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # retrieve - get
    def get(self,request):
        try:
            todos = Todo.objects.all()
            serializers = TodoSerializer(todos,many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class TodoDetailsView(APIView):
    # retrieve single todo - get
    def get(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializer(todo)
            return Response(serializers.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # update - put
    def put(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializer(todo,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=status.HTTP_200_OK)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # delete - delete
    def delete(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({"message":f"{todo.title} deleted successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CompleteView(APIView):
    def put(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            todo.completed = True
            return Response({"message":f"{todo.title} updated successfully"})
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)