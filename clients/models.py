from django.db import models
from django.core.exceptions import ValidationError

STATUS = (
    ('POTENTIAL', 'POTENTIAL'),
    ('STALLED', 'STALLED'),
    ('CANCELLED', 'CANCELLED'),
    ('IN_DISCUSSION', 'IN_DISCUSSION'),
    ('IN_PROGRESS', 'IN_PROGRESS'),
    ('COMPLETE', 'COMPLETE'),
    ('IN_UPSELL', 'IN_UPSELL'),
)

PROJECT_TYPE = (
    ('WEB_APP', 'WEB_APP'),
    ('PWA', 'PWA'),
    ('DESKTOP_APP', 'DESKTOP_APP'),
    ('WEBSITE', 'WEBSITE'),
    ('SOCIAL MEDIA MANAGEMENT', 'SOCIAL MEDIA MANAGEMENT'),
    ('TBD', 'TBD'),
)

TECHNOLOGY_STACK = (
    ('DJANGO_GRAPHQL & REACT_APOLLO', 'DJANGO_GRAPHQL & REACT_APOLLO'),
    ('NODE.JS & REACT & ELECTRON', 'NODE.JS & REACT & ELECTRON'),
    ('REACT', 'REACT'),
    ('HTML/CSS/JS', 'HTML/CSS/JS'),
    ('TBD', 'TBD'),
    ('N/A', 'N/A'),
)


def validate_numbers(rating):
    if rating not in range(0, 11):
        raise ValidationError(
            """Ratings should be between 1 and 10, with 10 as the best,
            the default is 0 for un-rated""")


class Client(models.Model):
    # fundamentals
    ordering = models.IntegerField(default=0)
    joined = models.DateField(auto_now=True)

    # client info
    business = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    # project details
    status = models.CharField(max_length=255, choices=STATUS)
    project_type = models.CharField(
        max_length=255, choices=PROJECT_TYPE, default=PROJECT_TYPE[0])
    technology_stack = models.CharField(
        max_length=255, choices=TECHNOLOGY_STACK, default=TECHNOLOGY_STACK[0])
    description = models.TextField(null=True, blank=True)

    # development details
    pivotal_tracker = models.URLField(max_length=255, null=True, blank=True)
    repositories = models.TextField(null=True, blank=True)
    dev_team = models.TextField(null=True, blank=True)
    project_docs = models.TextField(null=True, blank=True)

    # payments
    total_amount = models.CharField(max_length=255, null=True, blank=True)
    amount_paid = models.CharField(max_length=255, null=True, blank=True)
    amount_due = models.CharField(max_length=255, null=True, blank=True)

    # cash utilisation
    expenditure = models.TextField(null=True, blank=True)
    profit = models.TextField(null=True, blank=True)

    # timelines
    expected_start_date = models.DateField(null=True, blank=True)
    expected_duration = models.CharField(max_length=255, null=True, blank=True)
    expected_end_date = models.DateField(null=True, blank=True)
    actual_start_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    actual_duration = models.CharField(max_length=255, null=True, blank=True)

    # deployment
    product_urls = models.TextField(null=True, blank=True)

    # my rating and comments on the project/client
    project_complexity = models.IntegerField(
        validators=[validate_numbers], default=0)
    rate_client = models.IntegerField(validators=[validate_numbers], default=0)
    comments = models.TextField(null=True, blank=True)

    # client feedback
    rating = models.IntegerField(validators=[validate_numbers], default=0)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.business

    class Meta:
        ordering = ('ordering', )
