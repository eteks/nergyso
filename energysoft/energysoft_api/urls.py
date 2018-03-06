from django.conf.urls import url, include
# import oauth2_provider.views as oauth2_views
from django.conf import settings
# from .views import ApiEndpoint

from rest_framework import routers
from .views import EmployeeSet,EventsSet,NewsSet,FeedbackSet,ShoutoutPostSet,PasswordChangeView,NotificationSet,BannerSet,ShoutoutListSet,GalleryListSet,LiveTelecastSet,PollsSet,PollsResultPostSet,NotificationListSet,CEOMessageSet,SearchSet
from rest_framework.authtoken.views import obtain_auth_token
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet, GCMDeviceAuthorizedViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'employee', EmployeeSet)
router.register(r'events', EventsSet, base_name="events-search")
router.register(r'news', NewsSet, base_name="news-search")
router.register(r'notification', FCMDeviceAuthorizedViewSet)
# router.register(r'events/recent-events', NewsSet, name="recent_events")
router.register(r'device/gcm', GCMDeviceAuthorizedViewSet)
router.register(r'gallery', GalleryListSet, base_name="gallery")
router.register(r'livetelecast', LiveTelecastSet, base_name="livetelecast")
router.register(r'polls', PollsSet, base_name="polls")
router.register(r'shoutout_list', ShoutoutListSet, base_name="shoutout_list")
router.register(r'ceo_message_list', CEOMessageSet, base_name="ceo_message_list")

# OAuth2 provider endpoints
# oauth2_endpoint_views = [
#     url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
#     url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
#     url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
# ]

# if settings.DEBUG:
#     # OAuth2 Application Management endpoints
#     oauth2_endpoint_views += [
#         url(r'^applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
#         url(r'^applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
#         url(r'^applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
#         url(r'^applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
#         url(r'^applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
#     ]

#     # OAuth2 Token Management endpoints
#     oauth2_endpoint_views += [
#         url(r'^authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
#         url(r'^authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(),
#             name="authorized-token-delete"),
#     ]

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^o/', include(oauth2_endpoint_views, namespace='oauth2_provider')),
    # url(r'^api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^rest-auth/password/change/$', PasswordChangeView.as_view(),name='rest_password_change'),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^events/recent_events/', EventsSet.as_view({"get": "list"}), name="recent_events"),
    url(r'^events/search_events/(?P<search_string>.*)/', EventsSet.as_view({"get": "search_events"}), name="search_events"),
    url(r'^events/similar_events/(?P<pk>\d+)/', EventsSet.as_view({"get": "list"}), name="similar_events"),
    url(r'^news/recent_news/', NewsSet.as_view({"get": "list"}), name="recent_news"),
    url(r'^news/search_news/(?P<search_string>.*)/', NewsSet.as_view({"get": "search_news"}), name="search_news"),
    url(r'^feedback/', FeedbackSet.as_view({"post": "create"})),
    url(r'^shoutout_post/', ShoutoutPostSet.as_view({"post": "create"})),
    url(r'^shoutout/search_shoutout/(?P<search_string>.*)/', ShoutoutListSet.as_view({"get": "search_shoutout"}), name="search_shoutout"),
    # url(r'^shoutout_list/', ShoutoutListSet.as_view({"get": "list"})),
    url(r'^send_notification/', NotificationSet.as_view({"get": "list"}), name="send_notification"),
    url(r'^gallery_list/', GalleryListSet.as_view({"get": "list"})),
    url(r'^banner/', BannerSet.as_view({"get": "list"}), name="banners"),
    url(r'^employee/employee_tag_details/', EmployeeSet.as_view({"get": "list"}), name="employee_tag_details"),
    url(r'^employee/employee_today_birthday/', EmployeeSet.as_view({"get": "list"}), name="employee_today_birthday"),
    url(r'^employee/employee_upcoming_birthday/', EmployeeSet.as_view({"get": "list"}), name="employee_upcoming_birthday"),
    url(r'^employee/employee_today_anniversary/', EmployeeSet.as_view({"get": "list"}), name="employee_today_anniversary"),
    url(r'^employee/employee_upcoming_anniversary/', EmployeeSet.as_view({"get": "list"}), name="employee_upcoming_anniversary"),
    url(r'^pollsresult_post/', PollsResultPostSet.as_view({"post": "create"})),
    url(r'^polls_employee_result_exists/', PollsResultPostSet.as_view({"post": "retrieve"}), name="employee_result_exists"),
    url(r'^notification/notification_list_by_employee', NotificationListSet.as_view({"post": "retrieve"}), name="notification_list"),
    url(r'^notification/notification_status/(?P<pk>\d+)', NotificationListSet.as_view({"get": "notification_status"}), name="notification_status"),
    url(r'^ceo_message_post/', CEOMessageSet.as_view({"post": "create"})),
    # url(r'^ceo_message_list/', CEOMessageSet.as_view({"get": "list"})),
    url(r'^search/', SearchSet.as_view({"post": "retrieve"}), name="search_result"),
    url(r'^push_notification/create_device', NotificationSet.as_view({"post": "create"})),
    url(r'^push_notification/send_notification/', NotificationSet.as_view({"get": "send_notification"}), name="send_notification"),

    # Haystack and Elasticsearch
    # url(r'^events', EventsSet.as_view()),  # an example resource endpoint
]
	
