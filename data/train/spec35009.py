import numpy as np 

def function(x):

	w1 = x
	v4 = x
	paths = []
	try:
		if v4 > 8:
			w1 = w1*w1
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if v4 >= 6:
			v4 = 6/v4
			paths.append(3)
		else:
			x = 8-x
			v4 = w1*3
			v4 = w1+v4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))