from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            is_active=False
        )
        self.send_confirmation_email(user)
        return user

    def send_confirmation_email(self, user):
        subject = 'Your Confirmation Code'
        message = f'Your confirmation code is: {user.confirmation_code}'
        from_email = 'akimzanovmirislam@gmail.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)


class UserConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")

        if user.confirmation_code != data['confirmation_code']:
            raise serializers.ValidationError("Invalid confirmation code.")

        return data

    def save(self):
        user = User.objects.get(username=self.validated_data['username'])
        user.is_active = True
        user.confirmation_code = ""
        user.save()
        return user