import numpy as np 

def function(x):

	v5 = 7
	w9 = 8
	paths = []
	try:
		if x < 9:
			v5 = v5+x
			paths.append(1)
		else:
			x = x-x
			v5 = v5*x
			w9 = w9-w9
			paths.append(2)
		if x >= 4:
			x = x/w9
			v5 = 8/3
			w9 = v5-7
			paths.append(3)
		else:
			x = 1-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))