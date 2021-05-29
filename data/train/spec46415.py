import numpy as np 

def function(x):

	k3 = x
	r5 = x
	paths = []
	try:
		if r5 < 7:
			x = 5*6
			r5 = 4-x
			paths.append(1)
		else:
			k3 = k3/k3
			paths.append(2)
		if k3 > 2:
			r5 = r5+0
			x = 5-x
			paths.append(3)
		else:
			k3 = 5-1
			x = x+8
			k3 = 8*k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))