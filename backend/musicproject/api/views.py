# # api/views.py
# from django.shortcuts import get_object_or_404
# from rest_framework import permissions, status
# from rest_framework.response import Response
# from musicrecommend.models import Song  # Import Song from musicrecommend.models
# from .models import CustomUser  # Import CustomUser model
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate, login
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def register_user(request):
#     email = request.data.get('email')
#     password = request.data.get('password')
#     confirm_password = request.data.get('confirm_password')

#     # Simple validation
#     if not email or not password or not confirm_password:
#         return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

#     if password != confirm_password:
#         return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

#     serializer = UserSerializer(data=request.data)
    
#     if serializer.is_valid():
#         user = serializer.save()
#         return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login_user(request):
#     email = request.data.get('email')
#     password = request.data.get('password')

#     # Simple validation
#     if not email or not password:
#         return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         user = CustomUser.objects.get(email=email)
#     except CustomUser.DoesNotExist:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#     # Authenticate the user
#     user = authenticate(request, **{CustomUser.USERNAME_FIELD: email, 'password': password})

#     if user is not None:
#         login(request, user)
#         return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# class CheckUserView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)

#     def get(self, request):
#         if request.user.is_authenticated:
#             return Response({"message": "User is authenticated"})
#         else:
#             return Response({"message": "User is not authenticated"})