# TECH with OMID
This was my [blog](https://techwithomid.ir) source code writen in Django.

**DO NOT USE THE PROJEECT IN PRODUCTION**

## HOW TO USE PROJECT?
First of all you should define `DJANGO_SETTINGS_MODULE` for specify if project run in development environment or production.

The admin panel url is `/dj-admin`

#### Development 
Execute this in terminal for specify what setting file Django should use:
```bash
export DJANGO_SETTINGS_MODULE="two.settings.dev"
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Run the make migrations and migrate command:
```bash 
python manage.py makemigrations blog
python manage.py migrate
```


#### Production
Execute this in terminal for specify what setting file Django should use:
```bash
export DJANGO_SETTINGS_MODULE="two.settings" 
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Run the make migrations and migrate command:
```bash 
python manage.py makemigrations blog
python manage.py migrate
```
In production passenger wsgi file should change.

## TODO
- [ ] Update the gitignore file
- [ ] Better Documentation
- [ ] Config script for atumaticly config the workspace
- [x] Remove unnecessary comments
- [x] Delete unnecessary files
