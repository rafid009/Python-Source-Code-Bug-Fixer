import numpy as np 

def function(x):

	k3 = 0
	x2 = x
	paths = []
	try:
		if x <= 8:
			x2 = 8+2
			x2 = x2*1
			paths.append(1)
		else:
			x2 = x2*3
			paths.append(2)
		if x < 4:
			k3 = k3-6
			x2 = k3/2
			paths.append(3)
		else:
			x = x*7
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