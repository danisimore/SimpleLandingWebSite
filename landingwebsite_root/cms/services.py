from cms.models import CmsSlider


def get_slides():
    slider_list = CmsSlider.objects.all()
    return slider_list