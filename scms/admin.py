from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from .forms import GalleryMediaForm
from .models import Review,Reply,Subject, Page, ImageUpload, OurProject, SliderImage, Career, Author, News, GalleryImage, Gallery, GalleryMedia, EventManager, Event, MemberProfile, StudentProfile
from django.contrib.auth.models import User, Group
from auditlog.models import LogEntry
from django.contrib.admin.models import LogEntry


# Register your models here.
class PageAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug',  'link_text', 'group', 'content_access_level',  'published') 
    list_filter = ('published', 'page_type', 'group', 'content_access_level', 'page_type')
    search_fields = ('title', 'slug', 'navigation_text', 'page_title')
    prepopulated_fields = {'slug': ('title',)}


    fieldsets = (
        ('Meta Information', {
            'fields': ('title', 'slug', 'navigation_text', 'page_title', 'meta_description', 'meta_keywords')
        }),
        ('Content Section', {
            'fields': ('main_header', 'sub_header', 'page_type', 'link_text','enable_gallery', 'enable_uploads', 'body1', 'body2', 'body3', 'body4', 'extra_body', 'rich_intro', 'rich_body')
        }),
        ('Call to Action', {
            'fields': ('cta_header', 'cta_body', 'cta_action_text', 'cta_link_url')
        }),
        ('Attachments', {
            'fields': ('thumbnail', 'image', 'banner', 'seo_banner', 'attachment1', 'attachment2')
        }),
        ('Publish Settings', {
            'fields': ('category','group','page_layout','published_on', 'published', 'expires_on', 'content_access_level')
        }),
    )
    summernote_fields = ('rich_intro', 'rich_body')
    ordering = ('published_on',)
    
admin.site.register(Page, PageAdmin)




class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'image_preview', 'get_image_link')
    readonly_fields = ('image_preview', 'get_image_link')

    def image_preview(self, obj):
        """Display a small preview of the image."""
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: contain;" />',
                obj.image.url
            )
        return '(No Image)'

    def get_image_link(self, obj):
        """Provide the image link for copying."""
        if obj.image:
            return format_html(
                '<a href="{}" target="_blank">{}</a>',
                obj.image.url, obj.image.url
            )
        return '(No Image URL)'

    # Set descriptions for the admin panel
    image_preview.short_description = 'Image Preview'
    get_image_link.short_description = 'Image Link (Copy)'

# Register the admin class
admin.site.register(ImageUpload, ImageUploadAdmin)

class SliderImageInline(admin.TabularInline):
    model = SliderImage
    extra = 1

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

@admin.register(OurProject)
class OurProjectAdmin(admin.ModelAdmin):
    inlines = [SliderImageInline, GalleryImageInline]
    list_display = ('title', 'slug','thumbnail', 'tech_stack', 'project_link')
    
@admin.register(Career)
class CareerAdmin(SummernoteModelAdmin):
    list_display = ('title', 'job_type', 'requirement', 'posted_date', 'qualifications', 'last_date_to_apply', 'is_active')
    list_filter = ('job_type', 'is_active', 'posted_date', 'last_date_to_apply')
    search_fields = ('title', 'job_type', 'requirement')
    
    summernote_fields = ('description', 'responsibilities')
    ordering = ('-posted_date',)
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'active')  # Show active status in list view
    search_fields = ('name', 'email', 'phone')
    list_filter = ('active',)  # Add filter for active status
    list_editable = ('active',)
    


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published_at', 'active')
    search_fields = ('title', 'author__name', 'category')
    list_filter = ( 'active', 'category')
    prepopulated_fields = {'seo_title': ('title',)}
    

class GalleryMediaInline(admin.TabularInline):
    model = GalleryMedia
    extra = 1  # To display an empty form for adding a new media entry
    fields = ['image', 'caption']  # Specify which fields to display in the inline form

class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryMediaInline]
    list_display = ('title','thumbnail_preview', 'seo_title', 'active')
    prepopulated_fields = {'seo_title': ('title',)}
    search_fields = ('title', 'seo_title')
    list_filter = ('active',)

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" width="100" height="100" />', obj.thumbnail.url)
        return "No Thumbnail"
    thumbnail_preview.short_description = 'Thumbnail'

# Register the Gallery model with the custom admin
admin.site.register(Gallery, GalleryAdmin)

@admin.register(EventManager)
class EventManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'whatsapp_number', 'calling_timings')  # Fields displayed in the list view
    search_fields = ('name', 'email', 'contact')  # Searchable fields
    list_filter = ('calling_timings',)  # Filter by calling timings
    


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_manager', 'mode', 'start_date', 'end_date', 'active')  # Fields displayed in the list view
    list_filter = ('mode', 'start_date', 'active')  # Filter options
    search_fields = ('title', 'seotitle', 'event_manager__name')  # Searchable fields
    prepopulated_fields = {'seotitle': ('title',)}
    
    
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'object_id', 'object_repr', 'action_flag_display', 'change_message')
    list_filter = ('action_time', 'action_flag')
    search_fields = ('object_repr', 'change_message', 'object_id')

    # Human-readable action_flag
    def action_flag_display(self, obj):
        action_flags = {
            1: 'Added',
            2: 'Changed',
            3: 'Deleted',
        }
        return action_flags.get(obj.action_flag, 'Unknown')
    action_flag_display.short_description = 'Action'

    # Optionally, link to the object being modified (if possible)
    def object_url(self, obj):
        # Add your custom URL logic here if needed, based on `obj.object_id`
        return '-'

    object_url.short_description = 'Object URL'

admin.site.register(LogEntry, LogEntryAdmin)


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'designation', 'date_joined', 'active')
    search_fields = ('user__username', 'department', 'designation')
    list_filter = ('active', 'department')
    filter_horizontal = ('subjects',)
    
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number', 'course', 'year_of_study')
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "reviewer", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user__username", "reviewer__username", "review_description")

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"  
        
@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'responder', 'message', 'responded_at')
    search_fields = ('review__content', 'responder__username', 'message')
    list_filter = ('responded_at',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'credits', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('credits',)
    ordering = ('name',)
