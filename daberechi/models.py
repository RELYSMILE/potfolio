from django.db import models

class Home(models.Model):
    name = models.CharField(max_length=50)
    greetings_1 = models.CharField(max_length=20)
    greetings_2 = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to='picture/')
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.career
    
class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=50)
    social_link = models.URLField(max_length= 200)


class Category(models.Model):
    name = models.CharField(max_length=50)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

    def __str__(self) -> str:
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)




class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length= 200)

    def __str__(self) -> str:
        return f'Portfolio {self.id}'

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name