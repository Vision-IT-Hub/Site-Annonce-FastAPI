import psycopg2
import pandas as pd

from ..settings.secret_configs import get_secret

db_name = get_secret("DB_NAME")
user = get_secret("USER_NAME")
password = get_secret("PASSWORD")
host = get_secret("HOST")
port = get_secret("PORT")
conn = psycopg2.connect(
    database=db_name,
    user=user,
    password=password,
    host=host,
    port=port
)


def get_user(_id):
    _user = pd.read_sql(f'SELECT * FROM public."User" WHERE id = {_id} ', conn)
    conn.cursor().close()
    if _user.shape[0] == 0:
        return {}
    return _user.to_dict("records")
