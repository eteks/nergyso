from django.conf.urls import url, include
# import oauth2_provider.views as oauth2_views
from django.conf import settings
# from .views import ApiEndpoint

from rest_framework import routers
from .views import EmployeeSet,EventsSet,NewsSet,FeedbackSet,ShoutoutSet
from rest_framework.authtoken.views import obtain_auth_token
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'employee', EmployeeSet)
router.register(r'events', EventsSet, base_name="events-search")
router.register(r'news', NewsSet, base_name="news-search")
router.register(r'notification', FCMDeviceAuthorizedViewSet)
# router.register(r'events/recent-events', NewsSet, name="recent_events")

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
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^events/recent_events/', EventsSet.as_view({"get": "list"}), name="recent_events"),
    url(r'^events/similar_events/(?P<pk>\d+)/', EventsSet.as_view({"get": "list"}), name="similar_events"),
    url(r'^news/recent_news/', NewsSet.as_view({"get": "list"}), name="recent_news"),
    url(r'^feedback/', FeedbackSet.as_view({"post": "create"})),
    url(r'^shoutout/', ShoutoutSet.as_view({"post": "create"})),
    # Haystack and Elasticsearch
    # url(r'^events', EventsSet.as_view()),  # an example resource endpoint
]
	
