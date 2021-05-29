import numpy as np 

def function(x):

	v2 = x
	v9 = 2
	paths = []
	try:
		if v9 >= 1:
			v9 = v2+4
			v9 = 3+x
			v9 = 0/5
			paths.append(1)
		else:
			v9 = v9+4
			paths.append(2)
		if v2 > 6:
			v9 = v2+8
			v2 = v2+0
			paths.append(3)
		else:
			v2 = v2-7
			x = v9-x
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