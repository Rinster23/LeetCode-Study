# grid search
# args_list: a list of tuples
# kwargs_list: a list of dics
def parallel_jobs(n_jobs, func, args_list, kwargs_list):
    if len(args_list) == kwargs_list:
        pass
    if len(args_list) == 1:
        args_list = args_list * len(kwargs_list)
    if len(kwargs_list) == 1:
        kwargs_list = kwargs_list * len(args_list)
    from joblib import Parallel, delayed
    res_list = Parallel(n_jobs)(delayed(func)(*arg, **kwarg) for arg, kwarg in zip(args_list, kwargs_list))
    return res_list  # ordered


def task(a, b, c, d, e):
    pass


# i,j,k --> a,b,c
parallel_jobs(3, task, args_list=[(i, j, k) for i in range(3) for j in range(4) for k in range(4)],
              kwargs_list=[{'d': 6, 'e': 8}])
