from django.conf.urls import url

from verksamhetsplan.views import general as general_views
from verksamhetsplan.views import goal as goal_views
from verksamhetsplan.views import long_term_goal as long_term_goal_views
from verksamhetsplan.views import operational_plan as operational_plan_views

urlpatterns = [
    url('^$', general_views.index),
    url('^long_term/(?P<pk>\d+)/$',
        long_term_goal_views.long_term_goal_by_id, name='vp-long_goal'),
    url('^goal/(?P<pk>\d+)/$',
        goal_views.goal_by_id, name='vp-goal'),
    url('^(?P<year>[^/]+)/$',
        operational_plan_views.get_operational_plan, name='vp-operational_plan'),
    url('^(?P<year>[^/]+)/(?P<area_name>[^/]+)/$',
        operational_plan_views.get_operational_area, name='vp-operational_area'),
]
