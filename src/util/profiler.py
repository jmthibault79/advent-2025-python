import cProfile
import pstats
import sys
import io
from importlib import import_module


def profile_function(func=None, module_name: str = None, func_name: str = None, argv: list[str] = None) -> None:
    """
    Profile a function.
    
    Can be called in two ways:
    1. With a callable: profile_function(func=my_function, argv=['arg1', 'arg2'])
    2. With module/function names: profile_function(module_name='days.day10', func_name='part1', argv=['arg1'])
    
    Args:
        func: Callable to profile (mutually exclusive with module_name/func_name)
        module_name: Module to import (e.g., 'days.day10')
        func_name: Function name to profile (e.g., 'part1')
        argv: Arguments to pass to the function (optional)
    """
    if argv is None:
        argv = []
    
    # Get the function either directly or via dynamic import
    if func is not None:
        f = func
        func_label = getattr(func, '__name__', 'function')
    else:
        module = import_module(module_name)
        f = getattr(module, func_name)
        func_label = func_name
    
    # Setup sys.argv for the function
    original_argv = sys.argv
    sys.argv = [func_label] + argv
    
    try:
        # Create profiler and run the function
        profiler = cProfile.Profile()
        profiler.enable()
        
        f()
        
        profiler.disable()
        
        # Print statistics
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
        ps.print_stats(20)  # Print top 20 functions
        print(s.getvalue())
        
    finally:
        sys.argv = original_argv



