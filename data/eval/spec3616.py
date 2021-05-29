import numpy as np 

def function(x):

	w7 = x
	v1 = x
	x = x
	paths = []
	try:
		if v1 >= 1:
			x = 1/x
			paths.append(1)
		else:
			x = x/5
			x = x/x
			paths.append(2)
		if x < 2:
			x = v1/3
			v1 = x+8
			paths.append(3)
		else:
			v1 = w7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))