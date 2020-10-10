from GPyOpt.methods import BayesianOptimization
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#%matplotlib inline

# --- Define your problem
def f(x):
    #return (6*x-2)**2*np.sin(12*x-4)
    return -x*np.sin(x)+0.5*x

domain = [{'name': 'var_1', 'type': 'continuous', 'domain': (-5,5)}]

# --- Solve your problem : acquisition_type='EI','MPI'
myBopt = BayesianOptimization(f=f, domain=domain,acquisition_type='EI')

filepath = "gpyopt_img/img"
num = 5
for i in range(num):
    myBopt.run_optimization(max_iter=1)
    myBopt.plot_acquisition(filename=filepath+str(i)+".png")
    #myBopt.plot_acquisition(filename="gpyopt_img/img"+"{0:04d}".format(num)+".png")
print(myBopt.x_opt)
print(myBopt.fx_opt)

#################################################################################

fig = plt.figure()
ims = []

for i in range(num):
    im = plt.imread(filepath+str(i)+".png")
    ims.append([plt.imshow(im)])

ani = animation.ArtistAnimation(fig, ims, interval=1000)
plt.show()

###############################
#ani.save(filepath + "anim.gif")
#ani.save("anim.mp4")
