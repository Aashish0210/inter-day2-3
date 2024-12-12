from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        """
        This endpoint receives file metadata and saves it to the database.
        """
        file_data = request.data
        print(f"Received file data: {file_data}")

        if isinstance(file_data, list):
            return Response({"error": "Expected a dictionary of file data, not a list."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = FileSerializer(data=file_data)

        if serializer.is_valid():
            serializer.save()  # Save metadata in the database
            print(f"File '{file_data['name']}' uploaded successfully!")
            return Response({"message": "File metadata uploaded successfully."}, status=status.HTTP_201_CREATED)
        
        print(f"Error in file upload: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileSearchView(APIView):
    def get(self, request, *args, **kwargs):
        """
        This endpoint searches the database for file metadata based on query parameters.
        """
        search_query = request.query_params.get('search', None)
        
        if not search_query:
            return Response({"error": "Search query is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        files = File.objects.filter(name__icontains=search_query)
        
        if files.exists():
            serializer = FileSerializer(files, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No files found."}, status=status.HTTP_404_NOT_FOUND)


class FileDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        """
        This endpoint deletes a file based on the provided id.
        """
        file_id = kwargs.get('id')
        
        if not file_id:
            return Response({"error": "File id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            file_instance = File.objects.get(id=file_id)
            file_instance.delete()
            return Response({"message": f"File with id {file_id} deleted successfully."}, status=status.HTTP_200_OK)
        except File.DoesNotExist:
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
        
class FileUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        """
        This endpoint updates the file metadata based on the provided file ID.
        """
        file_id = kwargs.get('id')  # Extract file ID from the URL
        try:
            # Retrieve the file instance by its ID
            file_instance = File.objects.get(id=file_id)
        except File.DoesNotExist:
            return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the updated data and validate
        serializer = FileSerializer(file_instance, data=request.data, partial=True)  # 'partial=True' allows partial updates
        
        if serializer.is_valid():
            serializer.save()  # Save updated metadata to the database
            return Response({"message": f"File with id {file_id} updated successfully."}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)