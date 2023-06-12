from RealReturnsWeb import settings


def context_variables(request):
    return {"CURRENT_DOMAIN": settings.CURRENT_DOMAIN}
