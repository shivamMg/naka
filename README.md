### naka

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

   You can also add a whitelist of hostnames for CORS in the same file.
   ```json
   {
       "secret_key": "super-secret-key",
       "cors_origin_whitelist": [
           "127.0.0.1:3000",
           "localhost:3000"
       ]
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

7. Visit http://localhost:8000/api.


