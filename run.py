from instance import create_app
from app.api.v2.models.db import Db

db_object=Db()
app = create_app('default')
db_object.create_tables()
if __name__ == '__main__':
    app.run()
    