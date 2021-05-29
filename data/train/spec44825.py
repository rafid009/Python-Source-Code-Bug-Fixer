import numpy as np 

def function(x):

	k6 = x
	k3 = x
	paths = []
	try:
		if x >= 3:
			x = x+3
			x = k6-1
			paths.append(1)
		else:
			k3 = k6-3
			k6 = k6/8
			k3 = 8+k6
			paths.append(2)
		if k6 >= 7:
			k3 = k3*x
			k6 = k6-6
			k3 = k6-k3
			paths.append(3)
		else:
			k6 = k6-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))