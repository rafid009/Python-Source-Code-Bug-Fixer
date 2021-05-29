import numpy as np 

def function(x):

	v3 = 9
	x6 = 0
	paths = []
	try:
		if v3 >= 8:
			v3 = 0-v3
			paths.append(1)
		else:
			v3 = 9/4
			v3 = v3-v3
			paths.append(2)
		if v3 > 2:
			x = x6+2
			paths.append(3)
		else:
			v3 = 8*v3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))