import numpy as np 

def function(x):

	z7 = x
	v3 = x
	x = 6
	paths = []
	try:
		if v3 >= 1:
			x = x-3
			paths.append(1)
		else:
			v3 = v3+4
			x = x/z7
			paths.append(2)
		if x > 9:
			x = 3*x
			paths.append(3)
		else:
			v3 = 8-v3
			x = 9*x
			v3 = v3*4
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		v3 = z7**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))