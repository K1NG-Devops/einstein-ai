from django.db import models

class UserProgress(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    lesson = models.ForeignKey('robots.Lesson', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.lesson.title} - {self.completed}'
    
class Login(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.date_login}'
    
class Logout(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_logout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.date_logout}'
    
class PasswordChange(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_password_change = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.date_password_change}'
    
class UserCreation(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_user_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.date_user_creation}'
    
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/UserProfile', blank=True)

    def __str__(self):
        return self.user.username

