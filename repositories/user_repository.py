from db.run_sql import run_sql
from models.user import User


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
def select_all():  
    users = [] 

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    # create a list of user objects, from list of user dictionaries that have come back from run_sql.
    for row in results:
        # create a User object and then assign it to the user variable
        user = User(row['first_name'], row['last_name'], row['id'] )
        users.append(user)
    return users 


# READ - select one (by id)
def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    # Check if the user exists
    if result is not None:
        user = User(result['first_name'], result['last_name'], result['id'] )
    return user


# DELETE - delete one

def delete_all():
    sql = "DELETE  FROM users" 
    run_sql(sql)


# DELETE - delete all
def delete(id):
    sql = "DELETE  FROM users WHERE id = %s" 
    values = [id]
    run_sql(sql, values)


# UPDATE
def update(user):
    sql = "UPDATE users SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [user.first_name, user.last_name, user.id]
    run_sql(sql, values) 
