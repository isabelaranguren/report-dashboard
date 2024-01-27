from django.db import models
import uuid

# Create your models here.
class Client(models.Model):
    client_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client_name = models.CharField(max_length=255)
    client_url = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.client_name)
    
class Report(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    report_date = models.DateTimeField()
    summary = models.TextField()
    keywords_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Monthly Report for {self.client.client_name} dated {self.report_date}"
    
class Keyword(models.Model):
    keyword_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    keyword_text = models.CharField(max_length=255)

    def __str__(self):
        return self.keyword_text
    
class SearchEngineListing(models.Model):
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    # Fields to store the count of ranked keywords for each search engine
    google_desktop_keywords_count = models.IntegerField(default=0)
    google_mobile_keywords_count = models.IntegerField(default=0)
    yahoo_keywords_count = models.IntegerField(default=0)
    bing_keywords_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Ranked Keywords per Search Engine"
    
class VisibilityStatistics(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    first_position_count = models.IntegerField(default=0)
    top_five_positions_count = models.IntegerField(default=0)
    first_page_count = models.IntegerField(default=0)
    first_two_pages_count = models.IntegerField(default=0)
    new_listings_count = models.IntegerField(default=0)
    moved_up_count = models.IntegerField(default=0)
    moved_down_count = models.IntegerField(default=0)
    no_change_count = models.IntegerField(default=0)
    total_positions_gained_lost = models.IntegerField(default=0)

    def __str__(self):
        return f"Visibility Statistics for {self.report}"


class SERPPosition(models.Model):
    serp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    google_desktop_current_rank = models.IntegerField(null=True, blank=True)
    google_desktop_previous_rank = models.IntegerField(null=True, blank=True)
    google_desktop_url = models.URLField(max_length=2048, null=True, blank=True)

    google_mobile_current_rank = models.IntegerField(null=True, blank=True)
    google_mobile_previous_rank = models.IntegerField(null=True, blank=True)
    google_mobile_url = models.URLField(max_length=2048, null=True, blank=True)
    
    yahoo_url = models.URLField(max_length=2048, null=True, blank=True)
    yahoo_previous_rank = models.IntegerField(null=True, blank=True)
    yahoo_current_rank = models.IntegerField(null=True, blank=True)

    bing_previous_rank = models.IntegerField(null=True, blank=True)
    bing_url = models.URLField(max_length=2048, null=True, blank=True)
    bing_current_rank = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.keyword.keyword_text} - Serp Positions"