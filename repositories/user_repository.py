from db.run_sql import run_sql
from models.user import user


# CREATE
# paramaters: user is the user object
def save(user):
    # Returning id in this case, because we don't need all of the other data. Compare this with the '*' used in the task.py module.
    sql = "INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [user.first_name, user.last_name]
    results = run_sql(sql, values) # run_sql always returns a list (of dictionaries in this case - as we use DICT in run_sql)

    id = results[0]['id'] # index 0 of the list, and key "id" for the dictionary. This is the id for the newlhy created user.
    user.id = id
    return user


# READ - select all
# READ - select one (by id)
# UPDATE
# DELETE - delete one
# DELETE - delete all
