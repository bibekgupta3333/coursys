from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from oauth_provider.urls import urlpatterns as oauth_patterns
from courselib.urlparts import COURSE_SLUG
from coredata.api_views import MyOfferings, OfferingInfo

endpoint_v1_patterns = [
    url(r'^offerings$', MyOfferings.as_view()),
    url(r'^offerings/' + COURSE_SLUG + '$', OfferingInfo.as_view(), name='api.OfferingInfo'),
]
endpoint_v1_patterns = format_suffix_patterns(endpoint_v1_patterns)


api_patterns = [
  url(r'^1/', include(endpoint_v1_patterns)),
  url('', include(oauth_patterns)),
  #url(r'^docs/', include('rest_framework_swagger.urls')),
]