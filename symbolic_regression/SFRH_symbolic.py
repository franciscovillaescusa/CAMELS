import numpy as np
from gplearn.genetic import SymbolicRegressor
from gplearn.functions import make_function
import sys,os

def _pow(x1,x2):
    with np.errstate(over='ignore'):
        return _protected_exponent(x2*_protected_log(x1))

def _protected_exponent(x):
    with np.errstate(over='ignore'):
        return np.where(x < 30, np.exp(x), 1e15)

def _protected_log(x):
    with np.errstate(over='ignore'):
        return np.where(x > 1e-5, np.log(x), -11.0)

exp = make_function(function=_protected_exponent, name='exp', arity=1)
log = make_function(function=_protected_log,      name='log', arity=1)
pow = make_function(function=_pow,                name='pow', arity=2)

################################### INPUT ###########################################
root = '/mnt/ceph/users/camels/Results/neural_nets/params_2_SFRH'

f_SFRH   = '%s/SFRH_IllustrisTNG.npy'%root
f_params = '%s/params_IllustrisTNG.txt'%root

training_num = 700
testing_num  = 300

# symbolic regressor parameters
population_size       = 2000
generations           = 1000
tournament_size       = 20
function_set          = ('add', 'sub', 'mul', 'div', exp, log, pow, 
                         'cos', 'sin', 'tan', 'max', 'min')
metric                = 'mse'
init_depth            = (2, 10)
n_jobs                = 1
verbose               = 1
parsimony_coefficient = 0.0015
random_state          = None

# evolution parameters
# p_crossover + p_subtree_mutation + p_hoist_mutation + p_point_mutation <= 1.0
p_crossover        = 0.2
p_subtree_mutation = 0.25
p_hoist_mutation   = 0.2
p_point_mutation   = 0.25
p_point_replace    = 0.05

fout = 'results_59.txt'
#####################################################################################

# read SFRH and params
SFRH   = np.load(f_SFRH);       SFRH = np.log10(SFRH)
params = np.loadtxt(f_params)
z      = np.linspace(0, 7, 100)

##### training set #####
x_train = np.zeros((training_num*100,5), dtype=np.float32)
y_train = np.zeros((training_num*100, ), dtype=np.float32)

# do a loop over the different realizations
count = 0
for i in range(training_num):
    
    # do a loop over the different redshfits
    for j in range(100):
        x_train[count,0] = z[j]+1.0
        x_train[count,1] = params[i,0]
        x_train[count,2] = params[i,1]
        x_train[count,3] = params[i,2]
        x_train[count,4] = params[i,4]
        y_train[count]   = SFRH[i,j]
        count += 1
########################

##### testing set #####
x_test = np.zeros((testing_num*100,5), dtype=np.float32)
y_test = np.zeros((testing_num*100, ), dtype=np.float32)

# do a loop over the different realizations
count = 0
for i in range(training_num, training_num + testing_num):
    
    # do a loop over the different redshfits
    for j in range(100):
        x_test[count,0] = z[j]+1.0
        x_test[count,1] = params[i,0]
        x_test[count,2] = params[i,1]
        x_test[count,3] = params[i,2]
        x_test[count,4] = params[i,4]
        y_test[count]   = SFRH[i,j]
        count += 1
########################


# define model and hyperparameters
model = SymbolicRegressor(population_size=population_size, generations=generations,
                          tournament_size=tournament_size, function_set=function_set,
                          metric=metric, init_depth=init_depth,
                          verbose=verbose, parsimony_coefficient=parsimony_coefficient,
                          p_crossover=p_crossover, random_state=random_state,
                          p_subtree_mutation=p_subtree_mutation,
                          p_hoist_mutation=p_hoist_mutation,
                          p_point_mutation=p_point_mutation)

# fit the model
model.fit(x_train, y_train)

# training score
y_pred = model.predict(x_train)
mse_train = np.mean((y_pred - y_train)**2)
error_train = np.sqrt(np.mean((y_pred - y_train)**2/y_train**2))
print('mse train   = %.3e'%mse_train)
print('error train = %.3e'%error_train)

# testing score
y_pred = model.predict(x_test)
mse_test = np.mean((y_pred - y_test)**2)
error_test = np.sqrt(np.mean((y_pred - y_test)**2/y_test**2))
print('mse test = %.3e'%mse_test)
print('error test = %.3e'%error_test)

print(model._program)


# save results to file
f = open(fout,'w')

f.write('root         = %s\n'%root)
f.write('f_SFRH       = %s\n'%f_SFRH)
f.write('f_params     = %s\n'%f_params)
f.write('training_num = %s\n'%training_num)
f.write('testing_num  = %s\n\n'%testing_num)

f.write('population_size       = %s\n'%population_size)
f.write('generations           = %s\n'%generations)
f.write('tournament_size       = %s\n'%tournament_size)
f.write('function_set          = %s\n'%str(function_set))
f.write('metric                = %s\n'%metric)
f.write('init_depth            = %s\n'%str(init_depth))
f.write('n_jobs                = %s\n'%n_jobs)
f.write('verbose               = %s\n'%verbose)
f.write('parsimony_coefficient = %s\n'%parsimony_coefficient)
f.write('random_state          = %s\n\n'%random_state)

f.write('p_crossover        = %s\n'%p_crossover)
f.write('p_subtree_mutation = %s\n'%p_subtree_mutation)
f.write('p_hoist_mutation   = %s\n'%p_hoist_mutation)
f.write('p_point_mutation   = %s\n'%p_point_mutation)
f.write('p_point_replace    = %s\n\n'%p_point_replace)

f.write('mse train   = %.3e\n'%mse_train)
f.write('error train = %.3e\n'%error_train)
f.write('mse test    = %.3e\n'%mse_test)
f.write('error test  = %.3e\n'%error_test)

f.write('%s\n'%model._program)

f.close()
