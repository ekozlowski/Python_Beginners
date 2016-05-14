#!/usr/local/bin/python3
# encoding: utf-8
"""
A supervisor is using the TaskManagementSystem to manage tasks for his workers.
The system can add users, assign tasks to users, and get task(s) that belong
to a specific user.

You can not modify user or task class.
self.users and self.tasks in TaskManagementSystem has to remain as lists.
You can introduce new methods and class variables.

Goals:

DONE - Fix the syntax and semantic bugs that prevent the program from running correctly.

DONE - Change get_user_tasks() to return list of task names instead of task objects.

TODO: Add error handling to add_user(), add_task(), and get_user_tasks() methods

TODO: Optimize TaskManagementSystem to handle large number of users and tasks
"""


class User(object):

    def __init__(self, user_id, name):
        """
        Task object.  This code can not be modified.
            @ user_id: int
            @ name: string
        """
        self.user_id = user_id
        self.name = name


class Task(object):

    def __init__(self, user_id, task_name):
        """
        Task object.  This code can not be modified.
            @ user_id: int
            @ task_name: string
        """
        self.user_id = user_id
        self.task_name = task_name


class UserAlreadyExists(Exception):
    """
    Raised when an attempt is made to add a user to the TMS that already exists.
    """
    pass

class UserNotFoundException(Exception):
    """
    Raised when user lookup fails in TMS.
    """
    pass

class TaskManagementSystem(object):

    def __init__(self):
        self.users = {}  # Stores a dictionary of user objects, keyed by user name.  (This assumes we can't ever have
                         # two users with the same user name.)
        self.tasks = []  # stores a list of task objects
        # Since this is only at runtime, we can afford to just instantiate with a 0 value.  We would have to persist
        # this in an actual production system.
        self._uid = 0

    @property
    def unique_id(self):
        self._uid += 1
        return self._uid

    def add_user(self, user_name):
        """
        Add a new user
            @ user_name: string

        Condition:
            Every user should have a unique name
            Every user should have a unique id
        """
        if not isinstance(user_name, unicode):
            raise Exception("User name is not a unicode string")

        if user_name in self.users:
            raise UserAlreadyExists("User {} already exists in the TMS.".format(user_name))

        self.users[user_name] = User(user_id=self.unique_id, name=user_name)

    def add_task(self, user_name, task_name):
        """
        Add a task for a user
            @ user_name: string
            @ task_name: string

        Condition:
            The user should not have two or more tasks with the same name
        """
        # TODO:  Better task checking
        user = self.users.get(user_name)
        if user is None:
            raise UserNotFoundException("Could not find user {} to add task to.".format(user_name))

        self.tasks.append(Task(user.user_id, task_name))

    def get_user_tasks(self, user_name):
        """
        Get task(s) that belongs to the specified user name
            @ user_name: string
        """
        user_tasks = []
        user = self.users.get(user_name)
        if user is None:
            raise UserNotFoundException("Could not find user {} to get tasks from.".format(user_name))

        for task in self.tasks:
            if task.user_id == user.user_id:
                user_tasks.append(task)

        return [t.task_name for t in user_tasks]


if __name__ == "__main__":
    tms = TaskManagementSystem()
    tms.add_user(u'Bob')
    tms.add_task(u'Bob', u'laundry')
    tms.add_task(u'Bob', u'grocery')
    tms.add_task(u'Bob', u'daycare')
    tms.add_user(u'Ed')
    tms.add_user(u'Alisa')
    tms.add_user(u'Evan')
    print(tms.get_user_tasks('Bob'))
    for user in tms.users.values():
        print("Userid: {}, Name: {}".format(user.user_id, user.name))
    # should print: ['laundry', 'grocery', 'daycare']
