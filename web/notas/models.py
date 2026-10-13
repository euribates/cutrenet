
# Create your models here.
from wagtail.models import Page
from wagtail.fields import RichTextField


class Nota(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + ["body"]
