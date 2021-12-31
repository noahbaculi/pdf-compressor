from functools import wraps


def profiler(savefile=False):
    """Decorator to profile functions"""

    def profiler_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import cProfile
            import pstats

            prof = cProfile.Profile()
            ret_val = prof.runcall(func, *args, **kwargs)

            stats = pstats.Stats(prof)
            stats.sort_stats(pstats.SortKey.TIME)
            stats.print_stats()

            if savefile:
                from datetime import datetime
                print(f'{func.__name__} - {datetime.now():%m-%d-%Y %H:%M:%S}.profile')  # save profile file

            return ret_val
        return wrapper
    return profiler_dec


@profiler(savefile=False)
def func1(arg1, arg2):
    """Example function"""
    return arg1, arg2


if __name__ == "__main__":
    f1 = func1(131232, 192)
