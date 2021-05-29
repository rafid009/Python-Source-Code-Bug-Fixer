import numpy as np 

def function(x):

	p1 = 8
	k8 = 7
	paths = []
	try:
		if x > 1:
			p1 = 2*p1
			paths.append(1)
		else:
			k8 = 8-3
			p1 = 8-x
			paths.append(2)
		if p1 >= 7:
			x = p1/x
			paths.append(3)
		else:
			p1 = 2+k8
			k8 = 4-k8
			x = x*k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))