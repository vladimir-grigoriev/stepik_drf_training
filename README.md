Stepik DRF Lessons
==================
<https://stepik.org/course/73594/info>

1st week task
-------------

1) Making models;    `[DONE]`
1) Import data;    `[DONE]`
1) Getting product by pk;    `[DONE]`
1) Getting reviews;    `[DONE]`



## How to start

1. Clone project from github
    ```
    git clone https://github.com/vladimir-grigoriev/stepik_drf_training.git
    ```
2. Create `venv`
    ```zsh
    python3 -m venv env
    ```

3. Activate `venv`
4. Install requirements
    ```
    pip install -r requirements.txt
    ```
5. Move to src directory
    ```
    cd src/
    ```
6. Create a .env file with field
    ```
    SECRET_KEY='somerandomsymbols'
    ```
7. Run command
    ```
    python manage.py migrate
    ```
8. Create a superuser
    ```
    python manage.py createsuperuser
    ```
9. For adding data run
    ```
    python manage.py add_items
    python manage.py add_users
    python manage.py add_reviews
    ```