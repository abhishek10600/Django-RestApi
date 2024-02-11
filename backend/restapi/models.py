from django.db import models

# Create your models here.


class Company(models.Model):
    company_type = (('IT', 'IT'),
                    ('Non IT', 'Non IT'),
                    ('Manufacturing', 'Manufacturing'))

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=company_type)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ', ' + self.location


# create employee model
class Employee(models.Model):
    position_type = (('Manager', 'Manager'),
                     ('Developer', 'Developer'),
                     ('Marketing', 'Marketing'),
                     ('Sales', 'Sales'),
                     ('Project Lead', 'Project Lead'))

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.IntegerField()
    about = models.TextField()
    position = models.CharField(max_length=100, choices=position_type)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
