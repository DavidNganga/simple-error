from django.db import models

# Create your models here.
class Error(models.Model):
    name = models.CharField(max_length=250,null=True)
    error = models.CharField(max_length = 25,null = True)
    explanation = models.TextField(max_length=200,null=True)

    @classmethod
    def get_all(cls):
        errors = cls.objects.all()
        return errors

    def __str__(self):
        return self.name

    def save_error(self):
        self.save()

    def delete_error(self):
        self.delete()

    def get_Error_by_id(cls,id):
        bags = cls.objects.get(id=id)
        return bags

    @classmethod
    def search(cls,search_term):
         names = cls.objects.filter(name__icontains=search_term)
         return names

class Comment(models.Model):
    post = models.TextField(max_length=200,null=True)
    error = models.ForeignKey(Error, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.post

    def save_comment(self):
        self.save()

    @classmethod
    def get_all(cls):
        opinions = cls.objects.all()
        return opinions

    def get_Comment_by_id(cls,id):
        views = cls.objecs.get(id=id)
        return views
