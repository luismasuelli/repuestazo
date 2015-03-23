from django.contrib.admin import TabularInline, ModelAdmin, site
from .models import Banner, BannerType, ReelType, Reel, ReelImage


class BannerTypeAdmin(ModelAdmin):
    pass


class BannerAdmin(ModelAdmin):
    pass


class ReelTypeAdmin(ModelAdmin):
    pass


class ReelAdmin(ModelAdmin):
    """
    Muestra, de forma embebida, imagenes para ponerle al reel.
    """

    class InlineReelImageAdmin(TabularInline):
        model = ReelImage
        ordering = ('sequence',)
        exclude = ('reel_type',)
        min_num = 4

    inlines = [InlineReelImageAdmin]


class ReelImageAdmin(ModelAdmin):
    pass


site.register(BannerType, BannerTypeAdmin)
site.register(Banner, BannerAdmin)
site.register(ReelType, ReelTypeAdmin)
site.register(Reel, ReelAdmin)
site.register(ReelImage, ReelImageAdmin)