# import traceback
# from django.core.mail import send_mail
# import random
# from django.conf import settings
# from djangoproject.settings import EMAIL_HOST_USER
# from .models import OTP 

# def send_otp_email(email, otp):
#     subject = "Email Verification From Task App"
#     message = f"Your OTP for verifying your account is {otp}."
#     try:
#        send_mail(subject, message, "abhinethra.app.dev@gmail.com", [email],
#                  auth_password="lsns fwak loaz ingv",)
#     except Exception:
#         print("Error Sending OTP==============")
#         traceback.print_exc()
    



# def generate_otp(user):
    
#     otp_length = getattr(settings, 'OTP_LENGTH', 6)  # Default to 6-digit OTP
#     otp = ''.join(str(random.randint(0, 9)) for _ in range(otp_length))

#     otp_obj = OTP.objects.create(user=user, code=otp)

#     return otp_obj.code
