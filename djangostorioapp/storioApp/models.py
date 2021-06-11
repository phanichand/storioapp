from django.db import models

# Create your models here.

class Collection(models.Model):
   collection_name = models.CharField(max_length=200)
   collection_cover_image = models.ImageField(upload_to="images/")
   added_on = models.DateTimeField(auto_now_add=True)
   collection_back_color = models.CharField(max_length=200,null=True, blank=True)
   def __str__(self):
       return self.collection_name

class Story(models.Model):
   story_name = models.CharField(max_length=200)
   story_cover_image = models.ImageField(upload_to="images/")
   collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
   added_on = models.DateTimeField(auto_now_add=True)
   story_back_color = models.CharField(max_length=200,null=True, blank=True)
   def __str__(self):
       return self.story_name

class StoryPage(models.Model):
   story_page_no = models.IntegerField()
   story_page_text = models.CharField(max_length=500)
   story_page_image = models.ImageField(upload_to="images/")
   story_page_audio = models.FileField(upload_to="audios/",null=True, blank=True)
   story = models.ForeignKey(Story,  on_delete=models.CASCADE)
   added_on = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.story_page_text


class Promotions(models.Model):
    promotion_priority = models.IntegerField()
    promotion_title = models.CharField(max_length=100)
    promotion_description = models.CharField(max_length=100)
    promotion_image = models.ImageField(upload_to="images/")

    def __str__(self):
       return self.promotion_title


class Meaning(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.CharField(max_length=200)
    sentence_usage = models.CharField(max_length=200)
    word_image = models.ImageField(upload_to="images/")
    story = models.ForeignKey(Story,  on_delete=models.CASCADE)

    def __str__(self):
       return self.word

class Question(models.Model):
    question=models.CharField(max_length=500)
    story = models.ForeignKey(Story,  on_delete=models.CASCADE)
    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE,related_name="choices")
    choice = models.CharField("Choice", max_length=50)
    is_correct = models.BooleanField(default=False)
    #position = models.IntegerField("position")
