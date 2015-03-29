from django.contrib.admin import TabularInline, ModelAdmin
from repuestazo.admin import site
from .models import Banner, BannerType, ReelType, Reel, ReelImage, TextSetType, TextSetTypeField, TextSet, TextSetElement


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
        min_num = 4

    inlines = [InlineReelImageAdmin]


class ReelImageAdmin(ModelAdmin):
    pass


class TextSetTypeAdmin(ModelAdmin):
    """
    Muestra, de forma embebida, los campos que le pertenecen.
    """

    class InlineTextSetTypeFieldAdmin(TabularInline):
        model = TextSetTypeField
        ordering = ('code',)
        min_num = 4

    inlines = [InlineTextSetTypeFieldAdmin]


class TextSetAdmin(ModelAdmin):
    """
    Muestra, de forma embebida, los miembros que le pertenecen.
    """

    class InlineTextSetElementAdmin(TabularInline):
        model = TextSetElement
        ordering = ('code',)
        min_num = 4

    inlines = [InlineTextSetElementAdmin]


site.register(BannerType, BannerTypeAdmin)
site.register(Banner, BannerAdmin)
site.register(ReelType, ReelTypeAdmin)
site.register(Reel, ReelAdmin)
site.register(TextSetType, TextSetTypeAdmin)
site.register(TextSet, TextSetAdmin)
