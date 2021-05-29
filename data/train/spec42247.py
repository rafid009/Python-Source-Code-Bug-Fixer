import numpy as np 

def function(x):

	d2 = x
	k8 = x
	paths = []
	try:
		if d2 >= 9:
			x = 5*x
			x = x*7
			paths.append(1)
		else:
			d2 = d2*9
			paths.append(2)
		if k8 <= 4:
			d2 = 3/2
			paths.append(3)
		else:
			d2 = 9/7
			x = 2/7
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