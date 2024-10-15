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