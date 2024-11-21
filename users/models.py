from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields as needed
    subscription_valid = models.BooleanField(default=False)
    study_level = models.CharField(
        max_length=50,
        choices=[
            ('L1', '1ere annee L1'),
            ('L2', '2eme annee L2'),
            ('L3', '3eme annee L3/PASS'),
            ('DFASM1', '4eme annee DFASM 1'),
            ('DFASM2', '5eme annee DFASM 2'),
            ('DFASM3', '6eme annee DFASM 3'),
            ('Internat', 'Internat'),
            ('Medecin', 'Medecin'),
            ('Infirmier', 'Infirmier'),
            ('Pharmacien', 'Pharmacien'),
            ('Dentiste', 'Dentiste'),
            ('Autres', 'Autres'),
        ],
        null=True,
        blank=True,
    )
