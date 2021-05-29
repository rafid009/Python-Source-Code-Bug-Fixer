import numpy as np 

def function(x):

	k0 = x
	w9 = 0
	paths = []
	try:
		if x >= 8:
			k0 = k0-w9
			w9 = w9-5
			paths.append(1)
		else:
			w9 = 6+w9
			k0 = k0-k0
			paths.append(2)
		if k0 >= 0:
			x = x+x
			w9 = 5-w9
			paths.append(3)
		else:
			x = x/5
			k0 = 0-x
			k0 = 8-k0
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))