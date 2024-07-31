from django.shortcuts import render
from rest_framework import viewsets
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# Create your views here.
@api_view(['POST', 'OPTIONS'])
@authentication_classes([])
def register(request):
    """
    Register a new user.

    Args:
        request (Request): The request object containing user data.

    Returns:
        Response: A response object with success or error message.
    """
    if request.method == 'POST':
        user_data = request.data.copy()
        if 'name' not in user_data or 'email' not in user_data or 'password' not in user_data:
            return Response({'error': 'Missing required fields'}, status=400)
        
        user = User.objects.filter(email=user_data['email']).first()
        if user:
            return Response({'error': 'User already exists.'}, status=409)
        
        names = user_data['name'].split(' ')
        
        new_user = User(
            first_name=' '.join(names[:-1]),
            last_name=names[-1],
            email=user_data['email'],
            # phone_number=user_data.get('phoneNumber'),
        )
        new_user.set_password(user_data['password'])

        new_user.save()

        # current_site = get_current_site(request)
        # subject = "Welcome to Ecotrack"
        # html_message = render_to_string('new-email.html', {  
        # 'user': new_user,  
        # 'domain': current_site.domain,  
        # 'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),  
        # 'token':generate_token.make_token(new_user),  
        # })
        # plain_message = strip_tags(html_message)
        # email = EmailMultiAlternatives(
        #     from_email=settings.EMAIL_HOST_USER,
        #     to=[new_user.email],
        #     body=plain_message,
        #     subject=subject,
        # )
        # email.attach_alternative(html_message, 'text/html')
        # email.send()

        return Response({'message': 'User registered successfully', 'status': 201}, status=201)

@api_view(['GET', 'OPTIONS'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    """
    Get user information.
    """
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST', 'OPTIONS'])
@permission_classes([IsAuthenticated])
def create_course(request):
    """
    Create a new course.
    """
    user = request.user
    course = Course(user=user, name=request.data['name'], description=request.data['description'])
    course.save()

    return Response({'message': 'Course created successfully'}, status=status.HTTP_400_BAD_REQUEST)