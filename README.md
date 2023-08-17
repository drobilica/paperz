# hartija

RSS reader for drobilica


##Todo
#### Frontend
- [ ] active menu highlight
- [x] put wheather info somewhere 
- [ ] beautify weather 
- [ ] clean up templating and class names
- [x] generate right menu from yaml
- [x] limit number of characters to 500
- [ ] translation
- [ ] fix issue not snapping to 100% height
- [ ] make login
- [ ] edit list of subscriptions

#### Backend
- [x] put wheather info somewhere
- [x] on random news users see url which they are redirected
- [x] cache weather/air info (1hr) ( can be placed inside ext_data.json )
- [x] make cache for news if it doesn't exists when i click on `explore`
- [x] clean output for some sources
- [x] generate right menu from yaml
- [ ] translation
- [ ] make login
- [ ] edit list of subscriptions ( with status checks and list news)
- [ ] auto generate mtime for rss feeds

#### DevOps
- [x] dockerize it `make it`
- [ ] deploy to heroku,netapp or some serverless like that



* * *

#### Future improvements
- [ ] tailwind CSS instead of vanilla CSS
- [ ] Find pretty color theme
- [ ] users can choose themes
- [ ] users can chose subscriptions thumbnails

## RSS Feeder Sites
Site lists are located in app/data/rss-feeds.yaml

### Project structure

 - `conf` dir is for configuration
 - `app` dir is for logic/controller
 - `data` dir is for model/data
 - `static` dir is for static content and pages 

### API endpoints


#### GET

Get info on what news are available
`curl -X GET localhost:5000/api/cache`


Get info when cache is created
`curl -X GET localhost:5000/api/get_cache_info/`


#### Set
Make cache for individual category
`curl -X GET localhost:5000/api/cache/games`

Make cache for all 
`curl -X GET localhost:5000/api/generate_cache/`

