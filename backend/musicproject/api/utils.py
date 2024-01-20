# views.py
import pyotp
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_otp_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Check if the email is valid (you can add more validations)
        if not email:
            return JsonResponse({'error': 'Invalid email'}, status=400)

        # Generate a new TOTP secret
        totp = pyotp.TOTP(pyotp.random_base32())
        otp = totp.now()

        # Send OTP via email
        send_mail(
            'Subject: Your OTP',
            f'Your OTP is: {otp}',
            'from@example.com',  # Replace with your sender email address
            [email],  # Recipient's email address
            fail_silently=False,
        )

        return JsonResponse({'message': 'OTP sent successfully'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
