import numpy as np 

def function(x):

	k8 = x
	s9 = 4
	x = x
	paths = []
	try:
		if x <= 6:
			x = 8*x
			x = 2*x
			x = 6+x
			paths.append(1)
		else:
			x = x*4
			k8 = s9/k8
			k8 = 1*k8
			paths.append(2)
		if k8 > 1:
			k8 = k8*1
			k8 = 5*k8
			paths.append(3)
		else:
			k8 = 3+k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))