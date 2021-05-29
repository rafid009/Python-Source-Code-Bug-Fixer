import numpy as np 

def function(x):

	k3 = x
	v8 = x
	paths = []
	try:
		if x < 4:
			x = 3-k3
			paths.append(1)
		else:
			x = 7+v8
			k3 = 9*k3
			paths.append(2)
		if v8 >= 6:
			v8 = x-x
			x = 5-v8
			paths.append(3)
		else:
			x = k3+k3
			v8 = v8/8
			k3 = k3-k3
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