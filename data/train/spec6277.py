import numpy as np 

def function(x):

	v6 = 0
	j9 = x
	paths = []
	try:
		if v6 < 2:
			v6 = 2*v6
			v6 = 4+2
			paths.append(1)
		else:
			v6 = v6+j9
			x = x/v6
			paths.append(2)
		if v6 > 5:
			v6 = v6/x
			paths.append(3)
		else:
			j9 = j9+6
			j9 = j9-3
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