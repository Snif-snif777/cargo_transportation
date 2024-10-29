from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')
    brochure_url = models.URLField(blank=True, null=True)  # URL to downloadable brochure

    def __str__(self):
        return self.title


class FAQ(models.Model):
    service = models.ForeignKey(Service, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return f"{self.service.title} - FAQ: {self.question[:50]}..."

