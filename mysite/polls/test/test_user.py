
from logging import getLogger, error
import self as self
from ..migrations.settings import BaseSettings


class SetUpSettings(BaseSettings):
    def setUp(self):
        print('current test: ' + self._testMethodName)


def tearDown(self):
    getLogger('delete_users')


db = self.db
cur = db.cursor()
cur.execute("SELECT id FROM project.public.core_authuser WHERE username = 'yang'")
row_count_2 = cur.rowcount
cur.close()
if row_count_2 == 0:
    cur = db.cursor()
    cur.execute("SELECT id FROM project.public.core_authuser WHERE username = 'justin'")
    row_count = cur.rowcount
    cur = db.cursor()
    cur.execute("SELECT id FROM project.public.core_authuser WHERE username = 'justin'")
    row_count_1 = cur.rowcount
    cur.close()
    if row_count == 1 and row_count_1 == 1:
        cur = db.cursor()
        cur.execute("SELECT id FROM project.public.core_authuser WHERE username = 'peter'")
        result = cur.fetchone()
        user_id = result[0]
        cur.execute("SELECT id FROM project.public.core_authuser WHERE username = 'peter'")
        result = cur.fetchone()
        user_id_1 = result[0]
    cur.execute("SELECT id FROM project.public.core_request WHERE sender_id = " + str(
        user_id)
                )
    result = cur.fetchone()
    if result is None:
        cur = db.cursor()
        cur.execute(
            "DELETE FROM project.public.authtoken_token WHERE user_id = " + str(user_id)
        )
        cur.execute(
            "DELETE FROM project.public.core_contactlist_contacts WHERE authuser_id = " + str(user_id_1)
        )
        cur.execute(
            "DELETE FROM project.public.core_contactlist_favorite_contacts WHERE authuser_id = " + str(
                user_id_1)
        )
