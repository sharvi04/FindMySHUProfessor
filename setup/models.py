from django.db import models
from django.apps import apps
from django.utils.text import slugify



# Create your models here.


# country model
class Country(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
 
 #state model       
class State(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    country = models.ForeignKey('Country', on_delete=models.CASCADE, limit_choices_to={'status': 'active'})
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States'
        
#district model
class District(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    state = models.ForeignKey('State', on_delete=models.CASCADE, limit_choices_to={'status': 'active'})
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

#area model
class Area(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    district = models.ForeignKey('District', on_delete=models.CASCADE, limit_choices_to={'status': 'active'})
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
 
 
 #selectlist model       
class SelectList(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    type = models.CharField(max_length=100)  # No choices here
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    parent_key = models.CharField(max_length=100, blank=True, null=True)
    display_order = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.name} - {self.type} ({self.status})"


    class Meta:
        verbose_name = 'SelectList'
        verbose_name_plural = 'SelectLists'


#company model        
class Company(models.Model):
    ACTIVE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, blank=True, null=True)
    gst_tax_no = models.CharField(max_length=255, blank=True, null=True)
    pan_no = models.CharField(max_length=255, blank=True, null=True)
    upi_id = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company/logos/', blank=True, null=True)
    banner = models.ImageField(upload_to='company/banners/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='company/qr_codes/', blank=True, null=True)
    active = models.CharField(max_length=3, choices=ACTIVE_CHOICES, default='yes')

    address = models.TextField()
    bank_details = models.TextField()
    terms = models.TextField()
    note = models.TextField()
    footer = models.TextField()
    # Use string-based references for ForeignKey fields to avoid circular import issues
    country = models.ForeignKey('setup.Country', on_delete=models.CASCADE, limit_choices_to={'status': 'active'}, blank=True, null=True)
    state = models.ForeignKey('setup.State', on_delete=models.CASCADE, limit_choices_to={'status': 'active'}, blank=True, null=True)
    district = models.ForeignKey('setup.District', on_delete=models.CASCADE, limit_choices_to={'status': 'active'}, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

#branch model       
class Branch(models.Model):
    name = models.CharField(max_length=200) 
    code = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    company = models.ForeignKey('setup.Company', on_delete=models.CASCADE, limit_choices_to={'active': 'yes'})
    active = models.BooleanField(default=True)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Account(models.Model):
    name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=100)
    opening_balance = models.DecimalField(max_digits=12, decimal_places=2)
    bank_name = models.CharField(max_length=255)
    bank_contact_number = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    bank_address = models.TextField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    order = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    page_layout = models.CharField(max_length=255, blank=True, null=True)  # No FK here, will load dynamically
    description = models.TextField(blank=True, null=True)

    # SEO details
    seo_title = models.CharField(max_length=255, blank=True, null=True)
    seo_keywords = models.TextField(blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)

    # Attachments
    thumbnail = models.ImageField(upload_to='categories/thumbnails/', blank=True, null=True)
    image = models.ImageField(upload_to='categories/images/', blank=True, null=True)
    banner = models.ImageField(upload_to='categories/banners/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # If the slug field is not manually filled, generate it from the name
        if not self.slug:
            self.slug = slugify(self.name)  # Sluggify the name if slug is blank

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
