import numpy as np 

def function(x):

	k0 = x
	v6 = 4
	paths = []
	try:
		if v6 >= 2:
			x = x+0
			v6 = 2-v6
			paths.append(1)
		else:
			v6 = 2-v6
			paths.append(2)
		if v6 >= 2:
			v6 = v6-9
			v6 = x+v6
			paths.append(3)
		else:
			x = v6-v6
			k0 = k0*6
			x = 3/v6
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))