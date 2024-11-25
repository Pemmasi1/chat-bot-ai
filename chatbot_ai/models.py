from django.db import models

class BotResponse(models.Model):
    message = models.CharField(max_length=10000)

    def __str__(self):
        return f"{self.message}"


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)  # Customer's first name
    last_name = models.CharField(max_length=50)  # Customer's last name
    email = models.EmailField(unique=True)  # Customer's email (unique identifier)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    address = models.TextField(blank=True, null=True)  # Optional address
    city = models.CharField(max_length=50, blank=True, null=True)  # Optional city
    state = models.CharField(max_length=50, blank=True, null=True)  # Optional state
    country = models.CharField(max_length=50, blank=True, null=True)  # Optional country
    zip_code = models.CharField(max_length=10, blank=True, null=True)  # Optional ZIP code
    date_of_birth = models.DateField(blank=True, null=True)  # Optional date of birth
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the record was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the record was last updated

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

