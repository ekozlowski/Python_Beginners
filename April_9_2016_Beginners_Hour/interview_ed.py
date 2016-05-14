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


class TaskManagementSystem(object):

    def __init__(self):
        self.users = []  # stores a list of user objects
        self.tasks = []  # stores a list of task objects

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
        # TODO: Better Unique ID management
        # TODO: Check to see if users are already present
        unique_id = 0
        for u in self.users:
            if u.user_id > unique_id:
                unique_id = u.id

        self.users.append(User(unique_id, user_name))

    def add_task(self, user_name, task_name):
        """
        Add a task for a user
            @ user_name: string
            @ task_name: string

        Condition:
            The user should not have two or more tasks with the same name
        """
        # TODO:  Better User lookup
        # TODO:  Better task checking
        for user in self.users:
            if user.name == user_name:
                user_id = user.user_id

        self.tasks.append(Task(user_id, task_name))

    def get_user_tasks(self, user_name):
        """
        Get task(s) that belongs to the specified user name
            @ user_name: string
        """
        # TODO: Simplify Task lookup
        user_tasks = []

        # TODO: This is too many levels deep... Why?
        for user in self.users:
            if user.name == user_name:
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

    print tms.get_user_tasks('Bob')
    # should print: ['laundry', 'grocery', 'daycare']
