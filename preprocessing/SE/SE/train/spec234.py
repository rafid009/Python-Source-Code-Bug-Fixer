import numpy as np 

def function(x):

	k0 = 6
	v1 = x
	paths = []
	try:
		if v1 >= 3:
			x = v1*6
			paths.append(1)
		else:
			k0 = k0+6
			paths.append(2)
		if v1 < 4:
			x = x+v1
			k0 = k0-5
			paths.append(3)
		else:
			v1 = 1*3
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))