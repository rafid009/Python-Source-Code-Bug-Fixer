import numpy as np 

def function(x):

	k8 = x
	p3 = 9
	x = x
	paths = []
	try:
		if p3 >= 4:
			k8 = 7-0
			p3 = p3/k8
			x = 6*x
			paths.append(1)
		else:
			k8 = x*k8
			p3 = p3*7
			p3 = p3-5
			paths.append(2)
		if x >= 8:
			k8 = 4*k8
			paths.append(3)
		else:
			p3 = k8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))