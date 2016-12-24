### naka

#### Development Instructions

1. `cd` into the project directory and create a virtual environment.
   ```
   virtualenv -p `which python3` venv
   source venv/bin/activate
   ```
2. Install dependencies.
   ```
   pip install -r requirements.txt
   ```
3. Create a secrets file under `data` dir.
   ```
   mkdir data/conf
   touch data/conf/secrets.json
   ```
4. Edit `secrets.json` to add the secret key.
   ```
   {
       "secret_key": "super-secret-key"
   }
   ```
5. Migrate and create a super user.
   ```
   ./manage.py migrate
   ./manage.py createsuperuser
   ```
6. Run the development server.
   ```
   ./manage.py runserver
   ```
7. Visit http://localhost:8000/api.

