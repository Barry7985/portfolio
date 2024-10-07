from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la compétence")
    proficiency = models.IntegerField(verbose_name="Niveau de maîtrise", help_text="Niveau de 1 à 100")
    
    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=255, verbose_name="Établissement")
    degree = models.CharField(max_length=255, verbose_name="Diplôme")
    field_of_study = models.CharField(max_length=255, verbose_name="Domaine d'études")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(verbose_name="Date de fin", null=True, blank=True)
    
    def __str__(self):
        return f"{self.degree} en {self.field_of_study} à {self.institution}"

class Experience(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre du poste")
    company = models.CharField(max_length=255, verbose_name="Entreprise")
    description = models.TextField(verbose_name="Description du poste")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(verbose_name="Date de fin", null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} à {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre du projet")
    description = models.TextField(verbose_name="Description du projet")
    technologies = models.ManyToManyField(Skill, verbose_name="Technologies utilisées")
    start_date = models.DateField(verbose_name="Date de début du projet")
    end_date = models.DateField(verbose_name="Date de fin du projet", null=True, blank=True)
    project_url = models.URLField(verbose_name="URL du projet", null=True, blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField(verbose_name="Adresse email")
    phone_number = models.CharField(max_length=20, verbose_name="Numéro de téléphone", null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name="Adresse", null=True, blank=True)
    linkedin_url = models.URLField(verbose_name="LinkedIn", null=True, blank=True)
    github_url = models.URLField(verbose_name="GitHub", null=True, blank=True)
    
    def __str__(self):
        return self.email
