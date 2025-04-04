from django.db import models
from django.db import models
from django.utils.text import slugify
from setup.models import Category, SelectList
from auditlog.registry import auditlog
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



# Create your models here.


class Page(models.Model):
    # === Meta Section ===
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    navigation_text = models.CharField(max_length=255)
    page_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    # === Content Section ===
    
    main_header = models.CharField(max_length=255)
    sub_header = models.CharField(max_length=255, blank=True)
    enable_gallery = models.BooleanField(default=False)  
    enable_uploads = models.BooleanField(default=False)
  
    
    # Page Type dropdown (loading from SelectList model)
    page_type = models.CharField(max_length=50, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='PAGETYPE')])
    link_text = models.CharField(max_length=255, blank=True, null=True)

    # Conditional fields based on Page Type
    extra_body = models.TextField(blank=True, null=True)
    rich_intro = models.TextField(blank=True, null=True)
    rich_body = models.TextField(blank=True, null=True)
    teaser = models.TextField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    main_body = models.TextField(blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)


    # === Attachments ===
    thumb = models.ImageField(upload_to='uploads/thumbs/', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    banner = models.ImageField(upload_to='uploads/banners/', blank=True, null=True)

    # SEO Attachments
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    seo_banner = models.ImageField(upload_to='uploads/seo_banners/', blank=True, null=True)
    attachment1 = models.ImageField(upload_to='uploads/attachments/', blank=True, null=True)
    attachment2 = models.ImageField(upload_to='uploads/attachments/', blank=True, null=True)

    # === Call to Action ===
    cta_header = models.CharField(max_length=255, blank=True, null=True)
    cta_body = models.TextField(blank=True, null=True)
    cta_action_text = models.CharField(max_length=255, blank=True, null=True)
    cta_link_url = models.URLField(blank=True, null=True)

    # === Settings Section ===
    category = models.CharField(max_length=255, choices=[(cat.name, cat.name) for cat in Category.objects.all()])
    group = models.CharField(max_length=50, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='GROUP')])
    page_layout = models.CharField(max_length=50, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='LAYOUT')])

    # === Publish Section ===
    published_on = models.DateField()
    published = models.BooleanField(default=False)
    expires_on = models.DateField(null=True, blank=True)
    content_access_level = models.CharField(max_length=50, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='CONTENTACCESS')])

    # Auto slugify the title if slug is not provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        
auditlog.register(Page)        
        
class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
        
auditlog.register(ImageUpload)        

class OurProject(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the project")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="URL-friendly identifier (auto-generated from title)")
    thumbnail = models.ImageField(upload_to="thumbnails/", blank=True, null=True, help_text="Thumbnail image for the project")
    tech_stack = models.CharField(max_length=255, help_text="Technologies used (comma-separated)")
    description = models.TextField(help_text="Short description of the project")
    body = models.TextField(help_text="Detailed project body content")
    extra_body = models.TextField(blank=True, null=True, help_text="Additional details (optional)")
    project_link = models.URLField(blank=True, null=True, help_text="Link to the project (if applicable)")

    def save(self, *args, **kwargs):
        if not self.slug:  # Auto-generate slug if it’s not set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

auditlog.register(OurProject)

class SliderImage(models.Model):
    project = models.ForeignKey(OurProject, on_delete=models.CASCADE, related_name="slider_images")
    image = models.ImageField(upload_to="slider_images/", help_text="Upload a slider image")

    def __str__(self):
        return f"Slider Image for {self.project.title}"


auditlog.register(SliderImage)

class GalleryImage(models.Model):
    project = models.ForeignKey(OurProject, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ImageField(upload_to="gallery_images/", help_text="Upload a gallery image")

    def __str__(self):
        return f"Gallery Image for {self.project.title}"
        
auditlog.register(GalleryImage)        

class Career(models.Model):
    title = models.CharField(max_length=255, help_text="Job title (e.g., Software Engineer)")
    job_type = models.CharField(max_length=255, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='JOBTYPE')], help_text="Type of job")
    requirement = models.CharField(max_length=100, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='JOBREQUIREMENT')], help_text="Urgency of the requirement (e.g., 'Immediate')")
    description = models.TextField(help_text="Detailed job description")
    experience_required = models.CharField(max_length=100, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='JOBEXPERIENCE')], help_text="Relevant experience (e.g., '1 year and above')")
    responsibilities = models.TextField(help_text="Key responsibilities of the job")
    qualifications = models.CharField(max_length=255, choices=[(item.value, item.value) for item in SelectList.objects.filter(type='JOBQUALIFICATION')], help_text="Educational Qualifications")
    posted_date = models.DateField(auto_now_add=True, help_text="Date the job was posted")
    last_date_to_apply = models.DateField(blank=True, help_text="Deadline for job applications")
    is_active = models.BooleanField(default=True, help_text="Whether the job posting is active")

    def __str__(self):
        return self.title
        
auditlog.register(Career)   


class JobRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    apply_role = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')
    message = models.TextField()

    def __str__(self):
        return self.name
        
auditlog.register(JobRequest)          

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    insta_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
 
auditlog.register(Author)  
        
class News(models.Model):

    title = models.CharField(max_length=200)
    seo_title = models.SlugField(unique=True, blank=True)  # SEO-friendly title (slug)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    short_description = models.CharField(max_length=300, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)
    extra_body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True, null=True)  # Category field for organization
    active = models.BooleanField(default=True)  # Active status

    def save(self, *args, **kwargs):
        if not self.seo_title:
            self.seo_title = slugify(self.title)  # Auto-generate the slug if not provided
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'News Article'  # Singular name
        verbose_name_plural = 'News Articles'

auditlog.register(News)  
        

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='gallery_thumbnails/', blank=True, null=True)
    seo_title = models.SlugField(unique=True, blank=True)  # SEO-friendly title (slug)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.seo_title:
            self.seo_title = slugify(self.title)  # Auto-generate the slug if not provided
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

auditlog.register(Gallery)  


class GalleryMedia(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='media', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_media/')  # Ensure this is an ImageField
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption or f"Image in {self.gallery.title}"

auditlog.register(GalleryMedia)
        
class EventManager(models.Model):
    name = models.CharField(max_length=200)  # Name of the event manager
    avatar = models.ImageField(upload_to='event_manager_avatars/', blank=True, null=True)  # Profile picture/avatar
    contact = models.CharField(max_length=15)  # Primary contact number
    alt_contact = models.CharField(max_length=15, blank=True, null=True)  # Alternate contact number
    email = models.EmailField(unique=True)  # Email address
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)  # WhatsApp number
    calling_timings = models.CharField(max_length=100, blank=True, null=True)  # Available calling timings
    short_description = models.TextField(blank=True, null=True)  # Brief description of the event manager

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event Manager'
        verbose_name_plural = 'Event Managers'
        
auditlog.register(EventManager)


class Event(models.Model):
    MODE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    title = models.CharField(max_length=200)  # Event title
    seotitle = models.SlugField(unique=True, blank=True)  # SEO-friendly slug
    short_description = models.TextField(blank=True, null=True)  # Short description
    start_date = models.DateField()  # Start date of the event
    end_date = models.DateField(blank=True, null=True)  # End date of the event
    start_time = models.TimeField(blank=True, null=True)  # Start time of the event
    end_time = models.TimeField(blank=True, null=True)  # End time of the event
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)  # Online or offline
    event_manager = models.ForeignKey(
        'EventManager', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='events'
    )  # Link to the EventManager model
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # Event image
    banner = models.ImageField(upload_to='event_banners/', blank=True, null=True)  # Event banner
    body1 = models.TextField(blank=True, null=True)  # Detailed body content 1
    body2 = models.TextField(blank=True, null=True)  # Detailed body content 2
    extra_body = models.TextField(blank=True, null=True)  # Additional content
    event_invitation = models.FileField(upload_to='event_invitations/', blank=True, null=True)  # Event invitation file
    brochure = models.FileField(upload_to='event_brochures/', blank=True, null=True)  # Event brochure file
    active = models.BooleanField(default=True)  # Checkbox for active status

    def save(self, *args, **kwargs):
        if not self.seotitle:
            self.seotitle = slugify(self.title)  # Auto-generate slug if not provided
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        
auditlog.register(Event)


class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=50, unique=True, help_text="Unique subject code (e.g., MATH101)")
    credits = models.IntegerField(default=3, help_text="Number of credits for the subject")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    year_of_study = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='student_profiles/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.roll_number}"

auditlog.register(StudentProfile)



User = get_user_model()

class Review(models.Model):
    RATING_CHOICES = [
        (1, "1 - Poor"),
        (2, "2 - Fair"),
        (3, "3 - Good"),
        (4, "4 - Very Good"),
        (5, "5 - Excellent"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_received",
        limit_choices_to={'groups__name': "Member"}  
    )
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_given"
    )
    review_description = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"Review by {self.reviewer} for {self.user} - {self.get_rating_display()}"
        
auditlog.register(Review)

class Reply(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='replies')
    message = models.TextField()
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    responded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"

    def __str__(self):
        return f"Reply by {self.responder.username} on Review {self.review.id}"
        
auditlog.register(Reply)




auditlog.register(Subject)

class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member_profile')
    profile_picture = models.ImageField(upload_to='member_profiles/', blank=True, null=True, help_text="Profile picture of the professor")
    department = models.CharField(max_length=100, help_text="Department of the professor (e.g., Computer Science)")
    designation = models.CharField(max_length=100, help_text="Designation (e.g., Assistant Professor, Lecturer)")
    contact_number = models.CharField(max_length=15, blank=True, null=True, help_text="Contact number of the professor")
    office_address = models.TextField(blank=True, null=True, help_text="Office address of the professor")
    bio = models.TextField(blank=True, null=True, help_text="Short bio of the professor")
    date_joined = models.DateTimeField(auto_now_add=True, help_text="Date the professor joined the system")
    active = models.BooleanField(default=True, help_text="Whether the professor is currently active")
    subjects = models.ManyToManyField(Subject, blank=True, help_text="Subjects taught by the professor")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.department}"

auditlog.register(MemberProfile)