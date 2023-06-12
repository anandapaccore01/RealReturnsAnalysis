from django.urls import path
from userapp.views import home_views, reports_views, analysis_views

app_name = "userapp"

urlpatterns = [
    path("", home_views.home, name="home"),
    path("reports/", reports_views.reports, name="reports"),
    path("analysis/", analysis_views.analysis, name="analysis"),
    path("analysis/residential", analysis_views.residential, name="residential"),
    path("analysis/commercial/dscr", analysis_views.comm_dscr, name="comm-dscr"),
    path("analysis/commercial/roi", analysis_views.comm_roi, name="comm-roi"),
    path(
        "analysis/residential/dynupdate",
        analysis_views.residential_analysis,
        name="residential-analysis",
    ),
    path(
        "analysis/residential/save",
        analysis_views.save_residential_reports,
        name="save-residential-reports",
    ),
    path(
        "analysis/commercial/dscr/dynupdate",
        analysis_views.comm_dscr_analysis,
        name="comm-dscr-analysis",
    ),
    path(
        "analysis/commercial/dscr/save",
        analysis_views.save_comm_dscr_reports,
        name="save-comm-dscr-reports",
    ),
    path(
        "analysis/commercial/roi/dynupdate",
        analysis_views.comm_roi_analysis,
        name="comm-roi-analysis",
    ),
    path(
        "analysis/commercial/roi/save",
        analysis_views.save_comm_roi_reports,
        name="save-comm-roi-reports",
    ),
    path(
        "analysis/deleteTenant/<str:id>",
        analysis_views.delete_tenant,
        name="delete-tenant",
    ),
    path(
        "analysis/deleteTenantEscalations/<str:id>",
        analysis_views.delete_tenant_escalations,
        name="delete-tenant-escalations",
    ),
    path(
        "analysis/deleteAdditionalEscalations/<str:id>",
        analysis_views.delete_additional_escalations,
        name="delete-additional-escalations",
    ),
    path(
        "analysis/deleteSubheads/<str:id>",
        analysis_views.delete_subheads,
        name="delete-subheads",
    ),
]
