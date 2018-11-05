# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as plt


folder = '../../data/'
prefix = 'ff6dof_1_'

# Read the files
path = folder + prefix
q = np.loadtxt(path+'q.txt')
xh     = np.loadtxt(path+"LHand.txt")
xhdes  = np.loadtxt(path+"LHand_des.txt")
xlarm3 = np.loadtxt(path+"larm3.txt")
xlleg3 = np.loadtxt(path+"lleg3.txt")

# Set the plotting times
tf = 300
q = q[:tf,:];
#time = stime[:tf]
xh = xh[:tf,:]; xhdes = xhdes[:tf,:]
#xlarm3 = xlarm3[10:tf+10,:]

# Plot the temporal joint configuration
plt.plot(q[:,0], q[:,8:])
plt.xlabel('tiempo [s]')
plt.ylabel('Valor articular [rad]')
plt.title('Evolución articular en el tiempo')
plt.legend((r'$q_1$', r'$q_2$', r'$q_3$', r'$q_4$', r'$q_5$', r'$q_6$'), loc='best')
plt.grid()
plt.show()

# ---------------------
# Hand
# ---------------------
# Plot position
#plt.plot(x[:,0], x[:,1:4])
plt.subplot(121)
plt.plot(xh[:,0], xh[:,1], linewidth=2)
plt.plot(xh[:,0], xh[:,2], linewidth=2)
plt.plot(xh[:,0], xh[:,3], linewidth=2)
plt.plot(xhdes[:,0], xhdes[:,1:4],'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('posición [m]')
plt.title("Posición de la extremidad 1")
plt.legend(('x', 'y', 'z'), loc='best')
# plt.grid()
# plt.show()
# Plot orientation
plt.subplot(122)
plt.plot(xlarm3[:tf,0], xlarm3[11:tf+11,4], linewidth=2)
plt.plot(xlarm3[:tf,0], xlarm3[11:tf+11,5], linewidth=2)
plt.plot(xlarm3[:tf,0], xlarm3[11:tf+11,6], linewidth=2)
plt.plot(xlarm3[:tf,0], xlarm3[11:tf+11,7], linewidth=2)
xlarm3des = np.ones(xlarm3[:tf,4:].shape)
xlarm3des[:,0] = xlarm3[tf,4]*xlarm3des[:,0]
xlarm3des[:,1] = xlarm3[tf,5]*xlarm3des[:,1]
xlarm3des[:,2] = xlarm3[tf,6]*xlarm3des[:,2]
xlarm3des[:,3] = xlarm3[tf,7]*xlarm3des[:,3]
plt.plot(xlarm3[:tf,0], xlarm3des[:,0:], 'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('cuaternión')
plt.title('Orientación de la extremidad 1')
plt.legend((r'$\varepsilon_w$', r'$\varepsilon_x$', r'$\varepsilon_y$',
            r'$\varepsilon_z$'), loc="best")
#plt.axis('equal')
#plt.grid()
plt.show()


# ---------------------
# Leg
# ---------------------
# Plot position
#plt.plot(x[:,0], x[:,1:4])
plt.subplot(121)
plt.plot(xlleg3[:,0], xlleg3[:,1], linewidth=2)
plt.plot(xlleg3[:,0], xlleg3[:,2], linewidth=2)
plt.plot(xlleg3[:,0], xlleg3[:,3], linewidth=2)
#plt.plot(xhdes[:,0], xhdes[:,1:4],'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('posición [m]')
plt.title("Posición de la extremidad 2")
plt.legend(('x', 'y', 'z'), loc='best')
# plt.grid()
# plt.show()
# Plot orientation
plt.subplot(122)
plt.plot(xlleg3[:,0], xlleg3[:,4], linewidth=2)
plt.plot(xlleg3[:,0], xlleg3[:,5], linewidth=2)
plt.plot(xlleg3[:,0], xlleg3[:,6], linewidth=2)
plt.plot(xlleg3[:,0], xlleg3[:,7], linewidth=2)
#plt.plot(xlarm3[:tf,0], xlarm3des[:,0:], 'k--')
plt.xlabel('tiempo [s]')
plt.ylabel('cuaternión')
plt.title('Orientación de la extremidad 2')
plt.legend((r'$\varepsilon_w$', r'$\varepsilon_x$', r'$\varepsilon_y$',
            r'$\varepsilon_z$'), loc="best")
#plt.axis('equal')
#plt.grid()
plt.show()


# ---------------------
# Base
# ---------------------
# Plot position
#plt.plot(x[:,0], x[:,1:4])
plt.subplot(121)
plt.plot(q[:,0], q[:,1], linewidth=2)
plt.plot(q[:,0], q[:,2], linewidth=2)
plt.plot(q[:,0], q[:,3], linewidth=2)
plt.xlabel('tiempo [s]')
plt.ylabel('posición [m]')
plt.title("Posición de la base flotante")
plt.legend(('x', 'y', 'z'), loc='best')
plt.grid()
# plt.show()
# Plot orientation
plt.subplot(122)
plt.plot(q[:,0], q[:,4], linewidth=2)
plt.plot(q[:,0], q[:,5], linewidth=2)
plt.plot(q[:,0], q[:,6], linewidth=2)
plt.plot(q[:,0], q[:,7], linewidth=2)
plt.xlabel('tiempo [s]')
plt.ylabel('cuaternión')
plt.title('Orientación de la base flotante')
plt.legend((r'$\varepsilon_w$', r'$\varepsilon_x$', r'$\varepsilon_y$',
            r'$\varepsilon_z$'), loc="best")
#plt.axis('equal')
plt.grid()
plt.show()

