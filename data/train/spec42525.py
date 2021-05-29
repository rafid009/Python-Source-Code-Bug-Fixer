import numpy as np 

def function(x):

	k8 = x
	r1 = 9
	paths = []
	try:
		if r1 <= 5:
			r1 = 9+8
			paths.append(1)
		else:
			k8 = x*3
			k8 = k8/4
			k8 = k8+2
			paths.append(2)
		if k8 < 4:
			r1 = 7-k8
			paths.append(3)
		else:
			r1 = 4*r1
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))