import numpy as np 

def function(x):

	v2 = 6
	v9 = 3
	paths = []
	try:
		if v2 < 7:
			v9 = 5*7
			paths.append(1)
		else:
			v9 = v9*3
			paths.append(2)
		if v2 > 5:
			x = 9+x
			paths.append(3)
		else:
			v9 = v9*v2
			v9 = v9+0
			v9 = 8-v9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))