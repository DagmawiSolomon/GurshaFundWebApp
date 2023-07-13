from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count
from django.core.validators import MinValueValidator
# Create your models here.
User = get_user_model()
STATE_CHOICE = [
    ("Tigray", "Tigray"),
    ("Dire Dawa", "Dire Dawa"),
    ("Addis Ababa", "Addis Ababa"),
    ("Harari ", "Harari"),
    ("Gambella ", "Gambella "),
    ("SNNPR", "SNNPR"),
    ("Benishangul-Gumuz", "Benishangul-Gumuz"),
    ("Oromia", "Oromia"),
    ("Somali", "Somali"),
    ("Amhara", "Amhara"),
    ("Afar", "Afar"),
]
RECIPENT_CHOICE = [
    ("Yourself", "Yourself"),
    ("Someone else", "Someone else"),
    ("Charity", "Charity"),
]
CATEGORY_CHOICE = [
    ("All campaigns", "All campaigns"),
    ("Enviromental","Enviromental"),
    ("Medical","Medical"),
    ("Emergency","Emergency"),
    ("Education","Education"),
]
class Campaign(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, choices=STATE_CHOICE,  blank=True, null=True)
    city = models.CharField(max_length=100,  blank=True, null=True)
    recipent = models.CharField(max_length=100, choices=RECIPENT_CHOICE,  blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICE,  blank=True, null=True)
    goal = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = "uploads/", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_total_donations(self):
        total_donations = self.donations.aggregate(total_amount=Sum('amount'))
        return total_donations['total_amount'] or 0

    def get_total_donors(self):
        total_donors = self.donations.values('donor').distinct().count()
        return total_donors

    def closed(self):
        total_donations = self.get_total_donations()
        if str(total_donations) == self.goal:
            return True
        else:
            return False
    

class Donation(models.Model):
    amount = models.CharField(max_length=100, blank=True, null=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='donations')
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    date_donated = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"An amount of {self.amount} was donated to {self.campaign} by {self.donor}"
    

