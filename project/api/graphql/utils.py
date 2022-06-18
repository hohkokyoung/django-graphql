import copy
from graphql_relay import from_global_id

# this is a decorator function to provide a generic try-except error handling mechanism
# & it logs the full path to failed function in the case of a failure
# the default return value in any failure case is 'None', this value can be changed easily
# via the decorator argument
# credit: https://stackoverflow.com/questions/15572288/general-decorator-to-wrap-try-except-in-python
def handle_error(return_if_error=None, log_error=True, *args, **kwargs):
    def decorate(func):
        def applicator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # log where the exception is coming from
                if log_error:
                    print(f"Error in {func.__qualname__}:", e)
                return return_if_error

        return applicator

    return decorate

# helper function to decode a Relay global id back to django model object id
# with error handling
@handle_error(log_error=False)
def decode_global_id(id=None):
    return from_global_id(id)[1]


# for accessing deep nested json data in a safer way
def safe_get(dct, *keys):
    for key in keys:
        try:
            dct = dct[key]
        except (KeyError, IndexError):
            return None
        except:
            return None
    return dct

# a function that helps to remove all key-value pairs in the given dict using the given
# key names
def remove_from_dict(_dict, *keys):
    new_dict = copy.deepcopy(_dict)
    for key in keys:
        if key in new_dict:
            del new_dict[key]
    return new_dict