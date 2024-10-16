# SPX Endrance Fuel Advice Inteligence 
USe artifical inteligence to give nutrition advice based on user inputed constraints such as weight and duration of exersize.

## Deployment 

## Local Deployment 
Local deployment is done through a Dockerimage, hence the only local requirement id docker. 

### Docker (Recommended)
#### 1. Export env varaibles 
~~~bash
export OPENAI_API_KEY="your_api_key_here" 
# alternativly:  'source .env'
~~~

#### 2. Build and run Docker Image
~~~bash
docker build -t spx-net .

docker run spx-net
~~~

### Conda (For devolopers)

~~~bash 
# 1. Export env varaibles 

export OPENAI_API_KEY="your_api_key_here" 
# alternativly:  'source .env'

# 2. Install Requirements 
pip install -r requirements.txt

# 3. Run app


~~~

#### 1. Export env varaibles 
~~~bash
export OPENAI_API_KEY="your_api_key_here" 
# alternativly:  'source .env'
~~~

#### 2. Install Requirements 
~~~bash
pip install -r requirements.txt
~~~


## Strava Connection
  https://www.strava.com/oauth/authorize?client_id=137744&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all
 
 http://localhost/exchange_token?state=&code=f3cadfa35b9eb8401edb592e6b87c9cdacfcff25&scope=read,activity:read_all

  curl -X POST https://www.strava.com/oauth/token \
 -F client_id=137744 \
 -F client_secret=2ea62a8431df1bc6cd209efb744bda32257a23cd \
 -F code=f3cadfa35b9eb8401edb592e6b87c9cdacfcff25 \
 -F grant_type=authorization_code

 {"token_type":"Bearer","expires_at":1729107779,"expires_in":21600,"refresh_token":"3d53678202013bfd74abba7f423df6227a5047b6","access_token":"b7f7d91aa438067818423e8569e44fbadef8e1cf","athlete":{"id":2033770,"username":null,"resource_state":2,"firstname":"Bradford","lastname":"Gill","bio":"Longmeadow -\u003e SF","city":"San Francisco","state":"California","country":"United States","sex":"M","premium":true,"summit":true,"created_at":"2013-04-24T01:10:20Z","updated_at":"2024-10-03T02:33:57Z","badge_type_id":1,"weight":86.1825,"profile_medium":"https://dgalywyr863hv.cloudfront.net/pictures/athletes/2033770/839287/7/medium.jpg","profile":"https://dgalywyr863hv.cloudfront.net/pictures/athletes/2033770/839287/7/large.jpg","friend":null,"follower":null}}%  