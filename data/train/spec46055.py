import numpy as np 

def function(x):

	k3 = x
	r0 = x
	paths = []
	try:
		if x <= 7:
			k3 = r0+6
			paths.append(1)
		else:
			k3 = 7*x
			paths.append(2)
		if k3 >= 6:
			r0 = 3-r0
			r0 = x*7
			x = 2*0
			paths.append(3)
		else:
			k3 = 0/k3
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