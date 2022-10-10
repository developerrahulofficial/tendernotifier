from django.urls import path
from layout import views
urlpatterns = [
    # Vertical Layout
    path('Light-Sidebar',views.LightSidebarView.as_view(),name='light_sidebar'),
    path('Compact-Sidebar',views.CompactSidebarView.as_view(),name='compact_sidebar'),
    path('Icon-Sidebar',views.IconSidebarView.as_view(),name='icon_sidebar'),
    path('Boxed-Width-Sidebar',views.BoxWidthSidebarView.as_view(),name='boxed_width_sidebar'),
    path('Preloader-Sidebar',views.PreloaderSidebarView.as_view(),name='preloader_sidebar'),
    path('Colored-Sidebar',views.ColoredSidebarView.as_view(),name='colored_sidebar'),
    path('Scrollable',views.ScrollableSidebarView.as_view(),name='scrollable_sidebar'),

    #Horizontal Layout
    path('Horizontal',views.HorizontalView.as_view(),name='horizontal'),
    path('Horizontal-Light-Topbar',views.LightTopbarHoriView.as_view(),name='hori_topbar_light'),
    path('Horizontal-Boxed-Width',views.BoxedWidthHoriView.as_view(),name='hori_boxed_width'),
    path('Horizontal-Preloader',views.PreloaderHoriView.as_view(),name='hori_preloader'),
    path('Horizontal-Colored-Topbar',views.ColoredheaderHoriView.as_view(),name='hori_colored_header'),
    path('Horizontal-Scrollable',views.ScrollableHoriView.as_view(),name='hori_scrollable'),
]
