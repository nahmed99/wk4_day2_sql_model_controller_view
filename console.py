import pdb
from models.task import Task
from models.user import User
import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

task_repository.delete_all()
user_repository.delete_all()


jack = User("Jack", "Jarvis")
user_repository.save(jack)

victor = User("Victor", "McDade")
user_repository.save(victor)

dishes = Task("Do the dishes", jack, 4)
task_repository.save(dishes)


feed_cat = Task("Feed the cat", jack, 3)
task_repository.save(feed_cat)


pdb.set_trace()
