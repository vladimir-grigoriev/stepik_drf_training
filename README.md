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
5. Run commands
    ```
    python src/manage.py migrate
    ```
6. For adding data run
    ```
    python src/manage.py add_items
    python src/manage.py add_users
    python src/manage.py add_reviews
    ```