import numpy as np 

def function(x):

	k3 = x
	r9 = 1
	paths = []
	try:
		if x <= 2:
			k3 = k3+3
			r9 = r9/6
			x = x+r9
			paths.append(1)
		else:
			r9 = 6+r9
			k3 = k3-6
			paths.append(2)
		if k3 < 6:
			k3 = k3*k3
			r9 = r9*k3
			k3 = x-2
			paths.append(3)
		else:
			r9 = 6/r9
			r9 = r9*2
			r9 = 9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k3 = x**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))