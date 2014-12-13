import logging
logging.basicConfig()

def logging_decorator(func):
    def inner_function():
        log = logging.getLogger(func.__name__)
        try:
            func(log)
        except:
            log.exception('Exception calling: {}'.format(func.__name__))
    return inner_function

@logging_decorator
def bad_function(log):
    log.info('in_bad_function')
    1/0

@logging_decorator
def good_function(log):
    print 1+1

if __name__ == "__main__":
    good_function()
    bad_function()
