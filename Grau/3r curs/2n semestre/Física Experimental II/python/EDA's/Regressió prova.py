
# demo of regression without scipy
# (c) 2016 joan.masso@uib.es
import matplotlib.pyplot as plt
import numpy as np

def linear_regression(x,y):
	""" Fits y = Bx + A """
	n = x.size
	mx = x.mean()
	my = y.mean()
	sx = (x-mx).sum()
	sy = (y-my).sum()
	sxy = ( (x-mx)*(y-my) ).sum()
	sx2 = ((x-mx)**2).sum()
	sy2 = ((y-my)**2).sum()

	r = sxy/np.sqrt(sx2*sy2)
	b = sxy/sx2
	a = my - b*mx

	delta = np.sqrt( ((a + b*x - y)**2).sum() / (n-2) )
	err_a = delta * np.sqrt(1./n + mx*mx/sx2)
	err_b = delta * np.sqrt(1./sx2)

	return b,a,r,err_b,err_a

def plotlinreg(x, y, errorx, errory, a, b, err_a, err_b,r,
				title="Força magnètica respecte intensitat del conductor",xlabel="I(A)",ylabel="F(N)"):
	print ("Seguint el model: y = Bx + A, on 'y' és la força (N), 'x' és la intensitat (A), 'A' és el terme independent i 'B' és el pendent ")
	print ("r =",r,"r^2 = ",r**2)
	print ("b =",b,"a =",a)
	print ("err_b =",err_b," err_a =",err_a)
	
	# Plot the data
	fig = plt.figure()

	plt.plot(x, a + b*x ,'y--', label='$y={a:7.3f} + {b:7.3f}x$'.format(a=a,b=b))
	plt.errorbar(x,y,xerr=errorx,yerr=errory, fmt='r.')

	#plt.plot(x,(a+err_a) + (b+err_b)*x , 'r--')
	#plt.plot(x,(a-err_a) + (b-err_b)*x , 'r--')

	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title,loc='center',fontsize='12')
	#plt.legend(loc=2, fontsize=14)

	plt.show()

def demo():
    x1 = np.array([0.499, 1.003, 1.509, 2.007, 2.503, 3.010, 3.512, 4.016, 4.506, 5.002])
    y1 = np.array([0.000588, 0.001176, 0.001764, 0.002352, 0.002842, 0.003430, 0.004018, 0.004606, 0.005194, 0.005684])
    
    x2 = np.array([13, 27, 38, 49, 57])
    y2 = np.array([3.5, 6.0, 7.5, 10.5, 12.0])
	
	# Incerteses
    errorx = 0.001
    errory = 0.0001 # Calcular-ho...

	## Alternative which does not compute the error in a:
	# from scipy import stats
	# b, a,r ,p_value, err_b = stats.linregress(x,y)
	## then you can make the assumption
	# err_a = errory 
    b1,a1,r1,err_b1,err_a1 = linear_regression(x1,y1)
    b2,a2,r2,err_b2,err_a2 = linear_regression(x2,y2)

    plotlinreg(x1, y1, errorx,errory, a1,b1,err_a1,err_b1,r1)
    #plotlinreg(x2, y2, errorx,errory, a2,b2,err_a2,err_b2,r2)

if __name__ == '__main__':
	demo()

