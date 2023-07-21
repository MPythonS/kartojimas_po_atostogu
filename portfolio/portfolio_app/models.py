from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(
        max_length= 256)

    project_resume = models.CharField(
        max_length= 256)

    UTL_CHOICES = [
        ('PT', "Python"),
        ('CSS', "CSS"),
        ('JS', "Java Script"),
        ('DK', 'Docker'),
        ('DJ', "Django"),
        ('JSON', "JSON"),
        ('HT ', "HTML"),
        ('TK ', "TKInter"),
        ('SQ', "SQlite"),
        ('API', "API"),
        ('WS', "Web Scraping"),
        ('GT', "Git"),
        ('GH', "GitHub")]

    utl = models.CharField(
        max_length=4,
        choices=UTL_CHOICES,
        blank=False)

    utl1 = models.CharField(
        max_length=4,
        choices=UTL_CHOICES,
        blank=True)

    utl2 = models.CharField(
        max_length=4,
        choices=UTL_CHOICES,
        blank=True)

    utl3 = models.CharField(
        max_length=4,
        choices=UTL_CHOICES,
        blank=True)

    utl4 = models.CharField(
        max_length=4,
        choices=UTL_CHOICES,
        blank=True)

    utl5 = models.CharField(
        max_length=4,
        choices=UTL_CHOICES,
        blank=True)

    utl6 = models.CharField(
        max_length=4,
        choices=UTL_CHOICES,
        blank=True)

    utl7 = models.CharField(
        max_length=4,
        choices = UTL_CHOICES,
        blank=True)

    project_start_date = models.DateField(
        blank=False
    )

    PSTATUS_CHOICES = [
        ('K', "Kuriamas"),
        ('U', "Užbaigtas")]

    project_status = models.CharField(
        max_length= 1,
        choices= PSTATUS_CHOICES,
        blank=False
        )
    c_remarks = models.CharField(max_length=256, verbose_name='Pastabos', default='-')
    c_created_at = models.DateTimeField(auto_now_add=True)
    c_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.title}, {self.project_resume}, {self.project_start_date}"

