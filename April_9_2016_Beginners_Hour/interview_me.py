#!/usr/bin/env python2.7
# encoding: utf-8
"""
A supervisor is using the TaskManagementSystem to manage tasks for his workers.
The system can add users, assign tasks to users, and get task(s) that belong
to a specific user.

You can not modify user or task class.
self.users and self.tasks in TaskManagementSystem has to remain as lists.
You can introduce new methods and class variables.

Goals:
Fix the syntax and semantic bugs that prevent the program from running correctly.
Change get_user_tasks() to return list of task names instead of task objects.
Add error handling to add_user(), add_task(), and get_user_tasks() methods
Optimize TaskManagementSystem to handle large number of users and tasks
"""
from __future__ import print_function


class user(object):

    def __init__(self, user_id, name):
        """
        Task object.  This code can not be modified.
            @ user_id: int
            @ name: string
        """
        self.user_id = user_id
        self.name = name


class task(object):

    def __init__(self, user_id, task_name):
        """
        Task object.  This code can not be modified.
            @ user_id: int
            @ task_name: string
        """
        self.user_id = user_id
        self.task_name = task_name


class TaskManagementSystem(object):
    """
    Task System object.
        @ count: int
        @ user_dict: dict
    """
    count = 0  # counter for creating a new user id
    user_id_dict = {}  # stores key value pairs of users and their id
    user_task_dict = {}  # stores key value pairs of users and their tasks

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
        try:
            if user_name in self.user_id_dict:
                raise InputError
            
        except InputError:
            print('"{}" name was tried but already taken.'.format(user_name))
            
        else:
            self.users.append(user(self.count, user_name))
            self.user_id_dict[user_name] = self.count
            self.user_task_dict[user_name] = []
            self.count += 1

    def get_user_id(self, user_name):
        """
        Return a user id for a given user name.
            @ user_name: string
        """
        try:
            return self.user_id_dict[user_name]

        except KeyError:
            print('"{}" name does not exist.'.format(user_name))

    def get_task_list(self, user_name):
        """
        Return tasks for a given user name.
            @ user_name: string
        """
        try:
            return self.user_task_dict[user_name]

        except KeyError:
            print('"{}" name does not exist.'.format(user_name))

    def add_task(self, user_name, task_name):
        """
        Add a task for a user
            @ user_name: string
            @ task_name: string

        Condition:
            The user should not have two or more tasks with the same name
        """
        _user_id = self.get_user_id(user_name)
        if _user_id is None:
            raise LookupError("Couldn't find user")
        
        _tasks = self.get_task_list(user_name)
        
        try:
            if task_name not in _tasks:
                self.tasks.append(task(_user_id, task_name))
                self.user_task_dict[user_name].append(task_name)
            else:
                raise DuplicateError
        
        except DuplicateError:
            print('"{0}" task already exists for "{1}".'.format(
                                                        task_name, user_name))

    def get_user_tasks(self, user_name):
        """
        Get task(s) that belongs to the specified user name
            @ user_name: string
        """
        _user_id = self.get_user_id(user_name)

        return self.get_task_list(user_name)


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Raised when user inputs an invalid user_name."""
    pass


class LookupError(Error):
    """Raised when user_name does not exist."""
    pass


class DuplicateError(Error):
    """Raised when user_name does not exist."""
    pass


if __name__ == '__main__':

    tms = TaskManagementSystem()
    tms.add_user('Bob')
    tms.add_task('Bob', 'laundry')
    tms.add_task('Bob', 'grocery')
    tms.add_task('Bob', 'daycare')

    print(tms.get_user_tasks('Bob'))
    # should print: ['laundry', 'grocery', 'daycare']
    
