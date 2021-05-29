import numpy as np 

def function(x):

	v3 = 1
	w7 = 8
	paths = []
	try:
		if w7 >= 8:
			w7 = 1+w7
			paths.append(1)
		else:
			w7 = w7/8
			v3 = v3*7
			x = x*v3
			paths.append(2)
		if x <= 6:
			v3 = v3-9
			v3 = w7*v3
			paths.append(3)
		else:
			v3 = v3*9
			w7 = 7/w7
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