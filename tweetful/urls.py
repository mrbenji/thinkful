

API_URL = "https://api.twitter.com"
REQUEST_TOKEN_URL = API_URL + "/oauth/request_token"
AUTHORIZE_URL = API_URL + "/oauth/authorize?oauth_token={request_token}"
ACCESS_TOKEN_URL = API_URL + "/oauth/access_token"
TIMELINE_URL = API_URL + "/1.1/statuses/home_timeline.json"
GET_FOLLOWERS_URL = API_URL + "/1.1/followers/list.json"
GET_FRIENDS_URL = API_URL + "/1.1/friends/list.json"
POST_STATUS_URL = API_URL + "/1.1/statuses/update.json"
