# Photo Manager
Simple REST API for Photo Manager. Uses in-memory approach for data storing and not suitable for huge amount of data.
There is no authentication
Can be improved by plugging in DB and using at least basic auth. 
### Prerequisites
```
Python 3.5+
Virtualenv for you version of Python
```
### Installing
```
1. Clone repository
2. Navigate to the root of the repository
3. Create Python virtual environment from CLI: virtualenv env
4. Install Python requirements from CLI: env\Scripts\pip install -r requirements.txt
5. Run api.py from your favorite IDE or from CLI: env\Scripts\python 
```

### Running the tests

Application has full set of integration tests.
Tests can be executed from your favorite IDE or from CLI by navigating to the root of the project: 
```
env\Scripts\python -m unittest discover -s tests -v
```
### Available endpoint
```
/manager/init
/manager/albums
/manager/albums/<int:album_id>
/manager/album/<int:album_id>
/manager/photos
/manager/photos/<int:album_id>
/manager/photos/<int:album_id>/<int:photo_id>
/manager/reload
```