from rest_framework.throttling import UserRateThrottle

class ReveiwCreateThrottle(UserRateThrottle):
    scope='review-create'
    
class ReveiwListThrottle(UserRateThrottle):
    scope='review-list'
    
class ReveiwDetailsThrottle(UserRateThrottle):
    scope='review-details'
    
class StreamPlatformListThrottle(UserRateThrottle):
    scope='platform-list'
    
class StreamPlatformDetailsThrottle(UserRateThrottle):
    scope='platform-details'
    
class WatchListThrottle(UserRateThrottle):
    scope='watch-list'
    
class WatchDetailsThrottle(UserRateThrottle):
    scope='watch-details'