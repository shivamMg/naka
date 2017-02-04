### naka

#### Dependencies

[Phantomjs](http://phantomjs.org) is required for capturing screenshots of Project Websites. You may download and install it from [here](http://phantomjs.org/download.html). Create `data/media_root` directory for storing media assets. With `DEBUG` as `True`, these assets will be served by the development server. On production, serve them separately through a proxy server. `server_name` in `data/conf/secrets.json` can be set to generate full image URL.


#### Development Instructions

1. `cd` into the project directory and create a virtual environment.
   ```bash
   virtualenv -p `which python3` venv
   source venv/bin/activate
   ```

2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Create a secrets file under `data` dir.
   ```bash
   mkdir data/conf
   touch data/conf/secrets.json
   ```

4. Edit `secrets.json` to add the secret key.
   ```json
   {
       "secret_key": "super-secret-key"
   }
   ```

   You can also add a whitelist of hostnames for CORS. Allowed hosts and Server name can also be added in the same file.
   ```json
   {
       "secret_key": "super-secret-key",
       "cors_origin_whitelist": [
           "127.0.0.1:3000",
           "localhost:3000"
       ],
       "allowed_hosts": [
           "0.0.0.0",
           "localhost"
       ],
       "server_name": "http://localhost:8000"
   }
   ```

5. Migrate and create a super user.
   ```bash
   ./manage.py migrate
   ./manage.py createsuperuser
   ```

6. Run the development server.
   ```bash
   ./manage.py runserver
   ```

7. Visit [localhost:8000/api](http://localhost:8000/api).


#### Production Deployment

Install Production requirements, and collect static files in `data/static_root` directory. Fire up gunicorn to run the application. Serve static files through a reverse proxy server.

```bash
pip install -r requirements.prod.txt
./manage.py collectstatic
gunicorn naka.wsgi:application --name naka --bind 0.0.0.0:8000 --workers 3
```

